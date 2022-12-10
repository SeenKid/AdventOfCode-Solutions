data = open('input.txt').readlines()

steps = []
for line in data:
    if 'addx' in line:
        addx, n = line.strip().split(' ')
        steps.append(('addx', 0))
        steps.append(('addx', int(n)))
    else:
        steps.append(('addx', 0))

x = 1
sum = 0
crtScreen = [' ']*240
for index, step in enumerate(steps):
    if x - 1 <= index % 40 <= x + 1:
        crtScreen[index] = '#'

    if (index + 1 - 20) % 40 == 0:
        sum += (index + 1) * x

    x += step[1]
    
print(f'part 1: {sum}')
print('part 2:')
for r in range(6):
    row = crtScreen[r * 40: r * 40 + 40]
    print(''.join(row))