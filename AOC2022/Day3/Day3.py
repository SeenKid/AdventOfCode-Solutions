# This code was given by Zeltim#1337 | 303561134328381440

with open("input.txt") as f:
    input = f.read().splitlines()

def part1(input):
    sumOfPriorities = 0
    for rucksack in input:
        compartment1 = rucksack[0:(len(rucksack)//2)]
        compartment2 = rucksack[(len(rucksack)//2)::]
        for item in compartment1:
            if (item in compartment2):
                minus = 38 if item.isupper() else 96
                sumOfPriorities += ord(item) - minus
                break
    return sumOfPriorities

def part2(input):
    sumOfPriorities = 0
    for i in range(0, len(input),3):
        rucksack1, rucksack2, rucksack3 = input[i], input[i+1], input[i+2]
        for item in rucksack1:
            if (item in rucksack2 and item in rucksack3):
                minus = 38 if item.isupper() else 96
                sumOfPriorities += ord(item) - minus
                break
    return sumOfPriorities
        
print(part1(input))
print(part2(input))