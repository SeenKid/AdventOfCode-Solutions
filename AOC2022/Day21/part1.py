
import re
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        line = re.sub(r"([a-z]{4})",r"\1()", line)
        line = "def " + line
        line = re.sub(r":", r": return", line)
        exec(line)
print(int(root()))