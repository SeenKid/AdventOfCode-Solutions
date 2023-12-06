with open("input.txt", "r") as file:
    data = file.readlines()

seeds = [int(i) for i in data[0].strip().split(": ")[1].split(" ")]
mappings = []
for line in data[2:]:
    line = line.strip()
    if line.endswith(":"):
        mappings.append([])
    elif len(line) > 0:
        mappings[-1].append([int(i) for i in line.split(" ")])

[m.sort(key=lambda x: x[1]) for m in mappings]

res = 2**32
for x in seeds:
    for typemappings in mappings:
        for mapping in typemappings:
            if x >= mapping[1] and x < mapping[1] + mapping[2]:
                x = x - mapping[1] + mapping[0]
                break
    res = min(x, res)
print(res)