# This code was given by Zeltim#1337 | 303561134328381440

with open("input") as f:
    input = list(map(lambda x: x.replace("\n", ""), f.readlines()))
def part1(input):
    shape_scores = {"X": 1, "Y": 2, "Z": 3}
    outcome_scores = {"A": {"X":3, "Y": 6, "Z": 0}, "B": {"X": 0, "Y": 3, "Z": 6}, "C": {"X": 6, "Y": 0, "Z": 3}}
    score = 0
    for line in input:
        you = line.split(" ")[1]
        enemy = line.split(" ")[0]
        score += shape_scores[you]
        score += outcome_scores[enemy][you]
    return score
def part2(input):
    outcome_scores = {"X": 0, "Y": 3, "Z": 6}
    shape_scores = {"X": {"A": 3, "B": 1, "C": 2}, "Y": {"A": 1, "B": 2, "C": 3}, "Z": {"A": 2, "B": 3, "C": 1}}
    score = 0
    for line in input:
        you = line.split(" ")[1]
        enemy = line.split(" ")[0]
        score += outcome_scores[you]
        score += shape_scores[you][enemy]
    return score
print("PART 1:", part1(input))
print("PART 2:", part2(input))