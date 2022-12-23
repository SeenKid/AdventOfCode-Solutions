import re
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        if "root:" in line:
            m = re.findall("[a-z]{4}",line)
            func1 = eval(m[1])
            func2 = eval(m[2])
            continue
        line = re.sub(r"([a-z]{4})",r"\1()", line)
        line = "def " + line
        line = re.sub(r":", r": return", line)
        exec(line)

def humn(): return 1
f1_1 = func1()
def humn(): return 2
f1_2 = func1()

if f1_1 < f1_2:
    reverseDir = True
else:
    reverseDir = False

lowerBound = 0
upperBound = 1e16
f2 = func2()
while True:
    i = (upperBound + lowerBound) // 2
    def humn(): return i

    f1 = func1()

    if f1 > f2:
        if reverseDir:
            upperBound = i
        else:
            lowerBound = i
    elif f2 > f1:
        if reverseDir:
            lowerBound = i
        else:
            upperBound = i
    else:
        print(int(i))
        break