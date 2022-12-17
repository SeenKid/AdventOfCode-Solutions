rocks = [[(2 + 0j), (3 + 0j), (4 + 0j), (5 + 0j)],
         [(3 + 0j), (2 + 1j), (3 + 1j), (4 + 1j), (3 + 2j)],
         [(2 + 0j), (3 + 0j), (4 + 0j), (4 + 1j), (4 + 2j)],
         [(2 + 0j), (2 + 1j), (2 + 2j), (2 + 3j)],
         [(2 + 0j), (3 + 0j), (2 + 1j), (3 + 1j)]]

def cavern_height(cavern):
    return int(max(p.imag for p in cavern))

def is_valid_move(cavern, rock, pos):
    return all(0 <= (c + pos).real <= 6 for c in rock) and all(not c + pos in cavern for c in rock)

def add_rock(cavern, rock, wind, wi):
    pos = 1j * (cavern_height(cavern) + 4)
    while True:
        h_move, wi = 1 if wind[wi % len(wind)] == '>' else -1, wi + 1
        if is_valid_move(cavern, rock, pos + h_move):
            pos += h_move
        if is_valid_move(cavern, rock, pos - 1j):
            pos -= 1j
        else:
            cavern.update({c + pos for c in rock})
            return cavern, wi

def part1(rocks, wind):
    wi, cavern = 0, set({x for x in range(7)})
    for i in range(2022):
        cavern, wi = add_rock(cavern, rocks[i % 5], wind, wi)
    print(cavern_height(cavern))

cache = {}
def check_cache(cavern, rocks, i, wind, wi):
    height = cavern_height(cavern)
    key = (i % len(rocks), wi % len(wind))
    if key in cache:
        old_i, old_height = cache[key]
        if (int(1e12) - i) % (i - old_i) == 0:
            return (height +
                    int(1e12 - i) // (i - old_i) * (height - old_height))
    else:
        cache[key] = (i, height)

def part2(rocks, wind):
    i, wi, cavern = 0, 0, set({x for x in range(7)})
    while not (answer := check_cache(cavern, rocks, i, wind, wi)):
        cavern, wi = add_rock(cavern, rocks[i % 5], wind, wi)
        i += 1
    print(answer)

wind = open("input.txt").read()
part1(rocks, wind)
part2(rocks, wind)
