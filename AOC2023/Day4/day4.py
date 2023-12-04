"""
This code calculates a total value and a sum of values based on the contents of a file.
It reads the file "day4.txt" and performs calculations using the data in the file.
The code uses a dictionary to keep track of values for each line in the file.
The total value is calculated by finding the intersection between two sets of words in each line,
and then using the number of intersecting words to calculate a power of 2.
The sum of values is calculated by adding up the values in the dictionary and adding the number of lines in the file.
"""

file  = open("day4.txt").read().splitlines()

total = 0
D = dict()

for i, line in enumerate(file, 1):
    win  = set(line.split(':')[1].split('|')[0].split())
    mine = set(line.split('|')[1].split())
    w = len(mine.intersection(win))
    if w:
        total += 2**(w-1)

        for n in range(1, w+1):
            D[i+n] = D.get(i+n, 0) + 1 + D.get(i, 0)

print(total, sum(D.values())+len(file))