from collections import Counter

with open("input.txt") as f:
    m = [a.strip() for a in f.readlines()]

# Part 1
gamma   = int("".join([Counter([x[i] for x in m]).most_common(1)[0][0] for i in range(len(m[0]))]) ,2)
epsilon = int("".join([Counter([x[i] for x in m]).most_common()[-1][0] for i in range(len(m[0]))]), 2)
print(f"Consommation électrique du sous-marin : {gamma * epsilon}")

# Part 2
# for oxygen: switch = True
# for co2: switch = False
def rating(gas, switch):
    i = 0
    while len(gas) > 1:
        freq = Counter([x[i] for x in gas]).most_common()
        if (freq[0][1] == freq[1][1]) == switch:
            bit = freq[-1][0]
        else:
            bit = freq[0][0]
        gas = list(filter(lambda x: x[i] == bit, gas))
        i += 1
    return int(gas[0], 2)

oxygen = rating(m, True)
co2 = rating(m, False)
print(f"Évaluation de l'assistance vitale : {oxygen * co2}")