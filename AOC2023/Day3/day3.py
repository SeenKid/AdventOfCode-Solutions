import re
from functools import reduce
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "day3.txt")

def parse_input(data):
    """
    Parse the input and return the parsed data.

    Args:
        data (str): The input data as a string.

    Returns:
        list: The parsed data as a list of lists.
    """
    data_list = [list(line) for line in data.splitlines()]  # Turn the entire input into a grid
    return data_list

def find_number(x, line):
    """
    Check forward and backward on the line to find and return the full number.

    Args:
        x (int): The x-coordinate of the symbol.
        line (list): The line of symbols.

    Returns:
        str: The full number as a string.
    """
    number = [line[x]]
    for i in range(1, 3):  # Go max two before number
        if i >= 0 and line[x - i].isdigit():  # If the value is a number, add to front of list
            number.insert(0, line[x - i])
        else:
            break
    for i in range(1, 3):  # Go max two after number
        if i < len(line) and line[x + i].isdigit():  # If the value is a number, add to end of list
            number.append(line[x + i])
        else:
            break
    number = ''.join(number)  # Join list into a single number string
    return number

def check_around_symbol(x, y, data, part2=False):
    """
    Check the surrounding symbols of a given coordinate in a 2D data array.

    Parameters:
    - x (int): The x-coordinate of the symbol.
    - y (int): The y-coordinate of the symbol.
    - data (list): The 2D data array.
    - part2 (bool): Flag indicating whether to perform part 2 calculations.

    Returns:
    - int or None: The sum of surrounding numbers if part2 is False, or the product of two surrounding numbers if part2 is True. Returns None if the number of surrounding numbers is not 2 in part2 mode.
    """
    surrounding_numbers = []
    for i in range(y - 1, y + 2):  # Should only check one above and one below
        if not i < 0 and not i >= len(data):
            prev_digit = False  # If the previous check was a number, this is True and ignore current number
            for j in range(x - 1, x + 2):  
                if not j < 0 and not j >= len(data[i]):
                    if data[i][j].isdigit() and not prev_digit:
                        surrounding_numbers.append(int(find_number(j, data[i])))
                        prev_digit = True
                    if not data[i][j].isdigit():  # Reset prev_digit when value is not a digit
                        prev_digit = False
    if part2:  # Part 2 almost reused code, but asked for multiplication instead if only 2 surrounding numbers
        if len(surrounding_numbers) == 2:
            return reduce(lambda x, y: x*y, surrounding_numbers)
        else: 
            return None
    else:
        return sum(surrounding_numbers)

def part1(parsed_data):
    """
    Calculate the total value of symbols adjacent to each character in the parsed data.

    Args:
        parsed_data (list): A list of strings representing the parsed data.

    Returns:
        int: The total value of symbols adjacent to each character.
    """
    pattern = r'[^\w\s.]'
    total_value = 0
    for y, line in enumerate(parsed_data):
        for x, char in enumerate(line):
            if re.match(pattern, char):
                total_value += check_around_symbol(x, y, parsed_data)  # Add total of surrounding values to total value
    return total_value

def part2(parsed_data):
    """
    Calculate the total value based on the surrounding gears in the parsed data.

    Args:
        parsed_data (list): A list of strings representing the parsed data.

    Returns:
        int: The total value calculated based on the surrounding gears.
    """
    pattern = r'\*'
    total_value = 0
    for y, line in enumerate(parsed_data):
        for x, char in enumerate(line):
            if re.match(pattern, char):
                gear_ratio = check_around_symbol(x, y, parsed_data, True)
                if gear_ratio is not None:
                    total_value += gear_ratio
    return total_value

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - Total of part numbers is {answer1}")
    print(f"PART2 - Total of all gear ratios is {answer2}")