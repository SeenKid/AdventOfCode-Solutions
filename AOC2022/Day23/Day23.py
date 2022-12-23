with open('input.txt') as f:
    elves = set()
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        for j, c in enumerate(line):
            if c == '#':
                elves.add((j,i))

directions = [ (0, -1), (0, +1), (-1, 0), (+1, 0) ]

round = 0
while True:
    round += 1
    proposals = {}
    for x,y in elves:
        tiles_around = [
            (x-1, y-1),
            (x,y-1),
            (x+1, y-1),
            (x+1, y),
            (x+1, y+1),
            (x, y+1),
            (x-1,y+1),
            (x-1, y)
        ]

        elf_can_move = False
        for px,py in tiles_around:
            if (px, py) in elves:
                for dx, dy in directions:
                    pos_to_check = []
                    propose_move = True
                    for px, py in tiles_around:
                        if (dx == 0 and py - y == dy) or (dy == 0 and px -x == dx):
                            if (px, py) in elves:
                                propose_move = False
                                break
                    if propose_move:
                        if (x+dx, y+dy) in proposals:
                            proposals[(x+dx, y+dy)] = None
                        else:
                            proposals[(x+dx, y+dy)] = (x,y)
                        break
                # an elf can move only in one direction!
                break

    if not proposals:
        break
    for (px, py), elf in proposals.items():
        if elf:
            elves.remove(elf)
            elves.add((px, py))

    min_x = min([x for x,y in elves])
    max_x = max([x for x,y in elves])
    min_y = min([y for x,y in elves])
    max_y = max([y for x,y in elves])

    directions = directions[1:] + directions[:1]

    if round == 10:
        print('part 1:', (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves))

print('part 2:', round)