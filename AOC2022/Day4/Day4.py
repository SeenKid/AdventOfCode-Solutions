part1 = 0
part2 = 0

with open("input.txt") as input_file:
    _input = input_file.read().splitlines()

for line in _input:
    elf1 = [int(i) for i in line.split(",")[0].split("-")]
    elf2 = [int(i) for i in line.split(",")[1].split("-")]

    if all([elf2[0] <= i <= elf2[1] for i in elf1]):
        part1 += 1
    elif all([elf1[0] <= i <= elf1[1] for i in elf2]):
        part1 += 1

    if any([elf2[0] <= i <= elf2[1] for i in elf1]):
        part2 += 1
    elif any([elf1[0] <= i <= elf1[1] for i in elf2]):
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)