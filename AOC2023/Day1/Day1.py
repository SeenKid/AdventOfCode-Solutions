# Imports 
import re

"""
Read the contents of a file named 'day1.txt' and return a list of lines.

Returns:
    list: A list of strings representing each line in the file.
"""
def read_lines():
    with open('day1.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines

lines = read_lines()

def get_numbers_with_indices(line):
    """
    Returns a list of numbers with their corresponding indices in the given line.

    Parameters:
    line (str): The input line.

    Returns:
    list: A list of lists, where each inner list contains the index and the number found in the line.
    """

    num_with_indices = []

    for i, ch in enumerate(line):
        if ch.isalpha():
            continue
        num_with_indices.append([i, ch])
    return num_with_indices

def get_digits_with_indices(line):
    """
    Returns a list of lists containing the starting indices and corresponding digits
    for each occurrence of a number word in the given line.

    Args:
        line (str): The input line containing numbers.

    Returns:
        list: A list of lists, where each inner list contains the starting index and
        corresponding digit for each occurrence of a number word in the line.
    """
    num_mapping = {
        'one': '1',
        'two' : '2',
        'three': '3',
        'four' : '4',
        'five': '5',
        'six': '6',
        'seven' : '7',
        'eight': '8',
        'nine': '9',
    }
    digits_with_indices = []

    for number in num_mapping:
        for m in re.finditer(number, line):
            digits_with_indices.append([m.start(), num_mapping[number]])
    return digits_with_indices

def part1():
    """
    Calculate the sum in each line.

    Returns: prints the total sum.
    """
    total_sum = 0
    for line in lines:
        num_indices = get_numbers_with_indices(line)
        num_indices.sort(key=lambda x: x[0])
        total_sum += int(num_indices[0][1] + num_indices[-1][1])

    print(f'part1: {total_sum}')


def part2():
    """
    Calculate the sum of the first and last digits in each line of the input file.

    Returns: prints the total sum.
    """
    total_sum = 0
    for line in lines:
        num_indices = get_numbers_with_indices(line)
        digit_indices = get_digits_with_indices(line)
        all_indices = digit_indices + num_indices

        all_indices.sort(key=lambda x: x[0])

        total_sum += int(all_indices[0][1] + all_indices[-1][1])

    print(f'part2: {total_sum}')

# Launch
if __name__ == "__main__":
    part1()
    part2()
