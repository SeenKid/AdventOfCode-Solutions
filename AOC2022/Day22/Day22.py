import sys
import re

sys.setrecursionlimit(100000)

FILE = sys.argv[1] if len(sys.argv) > 1 else "input"


def part_one(maze, instructions):
    loc = (0, 0)  # Y, X
    direction = 0  # 0 is right, 1 is down, 2 is left, 3 is up.

    height = len(maze)
    width = len(maze[0])

    for (x, m) in enumerate(maze[0]):
        if m == 1:
            loc = (0, x)
            break

    for inst in instructions:
        if inst.isnumeric():
            val = int(inst)
            for _ in range(val):
                first_move = True
                new_loc = loc

                # Move until valid.
                while (
                    first_move
                    or new_loc[0] < 0
                    or new_loc[0] >= height
                    or new_loc[1] < 0
                    or new_loc[1] >= width
                    or maze[new_loc[0]][new_loc[1]] == 0
                ):
                    first_move = False
                    match direction:
                        case 0:
                            new_loc = (new_loc[0], new_loc[1] + 1)
                        case 2:
                            new_loc = (new_loc[0], new_loc[1] - 1)
                        case 1:
                            new_loc = (new_loc[0] + 1, new_loc[1])
                        case 3:
                            new_loc = (new_loc[0] - 1, new_loc[1])

                    if new_loc[0] < 0:
                        new_loc = (height - 1, new_loc[1])
                    elif new_loc[0] >= height:
                        new_loc = (0, new_loc[1])
                    elif new_loc[1] < 0:
                        new_loc = (new_loc[0], width - 1)
                    elif new_loc[1] >= width:
                        new_loc = (new_loc[0], 0)

                if maze[new_loc[0]][new_loc[1]] == 2:
                    # Halt. Don't move! There's a wall.
                    break

                loc = new_loc
        else:
            match inst:
                case "R":
                    direction = (direction + 1) % 4
                case "L":
                    direction = (direction - 1) % 4

    return 1000 * (loc[0] + 1) + 4 * (loc[1] + 1) + direction


def part_two(maze, instructions):
    loc = (0, 0)  # Y, X
    direction = 0  # 0 is right, 1 is down, 2 is left, 3 is up, relative to the MAP.
    curr_face = 1

    height = len(maze)
    width = len(maze[0])

    if height < 100:
        cube_size = 4
    else:
        cube_size = 50

    for (x, m) in enumerate(maze[0]):
        if m == 1:
            loc = (0, x)
            break

    # Figure out what the numberings are.
    new_maze = []
    sizings = []
    for _ in range(6):
        sizings.append([0, 0])

    for row in maze:
        new_row = []
        r = 0
        for (r, size) in enumerate(sizings):
            if size[0] < cube_size:
                break
        sizings[r][0] += 1

        for cell in row:
            if cell == 0:
                new_row.append((cell, -1))
            else:
                c = 0
                for (c, size) in enumerate(sizings):
                    if c >= r and size[1] < cube_size:
                        break
                if c != r and sizings[c][1] == 0:
                    sizings[c][0] += 1
                sizings[c][1] += 1
                new_row.append((cell, c + 1))
        for size in sizings:
            size[1] = 0

        new_maze.append(new_row)

    # print(sizings)
    # for row in new_maze:
    #     for (cell, val) in row:
    #         if cell == 0:
    #             print(" ", end="")
    #         else:
    #             print(val, end="")
    #     print("")

    # Hard coded.
    relations = {
        1: {"down": 3, "left": 4, "up": 6, "right": 2},
        2: {"up": 6, "left": 1, "right": 5, "down": 3},
        3: {"down": 5, "up": 1, "left": 4, "right": 2},
        4: {"up": 3, "left": 1, "right": 5, "down": 6},
        5: {"left": 4, "right": 2, "up": 3, "down": 6},
        6: {"left": 1, "right": 5, "up": 4, "down": 2},
    }

    for inst in instructions:
        if inst.isnumeric():
            val = int(inst)
            for _ in range(val):
                new_loc = loc
                old_direction = direction
                old_face = curr_face
                match direction:
                    case 0:
                        new_loc = (new_loc[0], new_loc[1] + 1)
                        key = "right"
                    case 2:
                        new_loc = (new_loc[0], new_loc[1] - 1)
                        key = "left"
                    case 1:
                        new_loc = (new_loc[0] + 1, new_loc[1])
                        key = "down"
                    case 3:
                        new_loc = (new_loc[0] - 1, new_loc[1])
                        key = "up"

                # If moved off the board, correct by wrapping to a new face.
                if (
                    new_loc[0] < 0
                    or new_loc[0] >= height
                    or new_loc[1] < 0
                    or new_loc[1] >= width
                    or new_maze[new_loc[0]][new_loc[1]][0] == 0
                ):
                    new_face = relations[curr_face][key]
                    match (curr_face, new_face):
                        case (1, 6):
                            new_loc = (new_loc[1] - 50 + 150, 0)
                            direction = 0
                        case (1, 4):
                            new_loc = (149 - new_loc[0], 0)
                            direction = 0
                        case (2, 6):
                            new_loc = (height - 1, new_loc[1] - 100)
                            direction = 3
                        case (2, 5):
                            new_loc = (149 - new_loc[0], 99)
                            direction = 2
                        case (2, 3):
                            new_loc = (new_loc[1] - 100 + 50, 99)
                            direction = 2
                        case (3, 4):
                            new_loc = (100, new_loc[0] - 50)
                            direction = 1
                        case (3, 2):
                            new_loc = (49, new_loc[0] + 50)
                            direction = 3
                        case (5, 2):
                            new_loc = (149 - new_loc[0], 149)
                            direction = 2
                        case (5, 6):
                            new_loc = (new_loc[1] - 50 + 150, 49)
                            direction = 2
                        case (4, 3):
                            new_loc = (new_loc[1] + 50, 50)
                            direction = 0
                        case (4, 1):
                            new_loc = (149 - new_loc[0], 50)
                            direction = 0
                        case (6, 1):
                            new_loc = (0, 50 + new_loc[0] - 150)
                            direction = 1
                        case (6, 5):
                            new_loc = (149, new_loc[0] - 150 + 50)
                            direction = 3
                        case (6, 2):
                            new_loc = (0, new_loc[1] + 100)
                    curr_face = new_face
                else:
                    curr_face = new_maze[new_loc[0]][new_loc[1]][1]

                if new_maze[new_loc[0]][new_loc[1]][0] == 2:
                    # Halt. Don't move! There's a wall.
                    if curr_face != old_face:
                        direction = old_direction
                        curr_face = old_face
                    break
                loc = new_loc
        else:
            match inst:
                case "R":
                    direction = (direction + 1) % 4
                case "L":
                    direction = (direction - 1) % 4

    return 1000 * (loc[0] + 1) + 4 * (loc[1] + 1) + direction


def main():
    print(f"Using file {FILE}")
    with open(FILE, "r", encoding="utf-8") as f:
        reading_path = False
        maze = []
        instructions = []

        for line in f:
            line = line.strip("\n")
            if line == "":
                reading_path = True
                continue

            if reading_path:
                instructions = re.split(r"(\d+)", line)[1:-1]
            else:
                row = []
                for r in line:
                    if r == " ":
                        row.append(0)
                    elif r == ".":
                        row.append(1)
                    else:
                        row.append(2)
                maze.append(row)

        # Normalize widths.
        l = 0
        for row in maze:
            l = max(l, len(row))

        for (i, row) in enumerate(maze):
            maze[i] = row + [0] * (l - len(row))

        print(f"Part one: {part_one(maze, instructions)}")
        print(f"Part two: {part_two(maze, instructions)}")


main()