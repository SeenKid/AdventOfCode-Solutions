def detect(stream, length):
    offset = length - 1
    i = offset
    while i < len(stream):
        chars = set(stream[i-offset:i+1])
        if len(chars) == length:
            return i + 1
        i += 1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        stream = f.read().strip()

    print(f'Part 1: {detect(stream, length=4)}')
    print(f'Part 2: {detect(stream, length=14)}')