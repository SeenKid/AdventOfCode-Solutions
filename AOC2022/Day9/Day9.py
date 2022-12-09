rope = [0] * 10
seen = [set([x]) for x in rope]
sign = lambda x: (x>0) - (x<0)

for line in open('input.txt'):
    d, n = line.split()

    for _ in range(int(n)):
        rope[0] += {'L':+1, 'R':-1, 'D':1j, 'U':-1j}[d]

        for i in range(1, 10):
            dist = rope[i-1] - rope[i]
            if abs(dist) >= 2:
                rope[i] += complex(sign(dist.real), sign(dist.imag))
                seen[i].add(rope[i])

part1 = len(seen[1])
part2 = len(seen[9])

print (f"part 1 : {part1} \npart 2 : {part2}")