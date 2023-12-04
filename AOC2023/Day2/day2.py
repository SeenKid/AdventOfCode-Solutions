from common_code import read_file_lines
import math

COLOURS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def parse_game(game):
    """
    Parses the game string and checks if the colors are valid.

    Args:
        game (str): The game string in the format "color1: n1, color2: n2, ...".

    Returns:
        bool: True if all colors are valid, False otherwise.
    """
    extractions = game.split(":")[1].split(";")
    for extraction in extractions:
        colors = extraction.split(",")
        for color in colors:
            n, c = color.strip().split(" ")
            if COLOURS[c] < int(n):
                return False
    
    return True


def parse_game_min_colors(game):
    """
    Parses the game string and returns a dictionary containing the minimum number of each color required.

    Args:
        game (str): The game string in the format "color1: n1, color2: n2, ...".

    Returns:
        tuple: A tuple containing a boolean value indicating success and a dictionary with the minimum number of each color required.
    """
    colours_min = {k: 0 for k in list(COLOURS.keys())}
    extractions = game.split(":")[1].split(";")
    for extraction in extractions:
        colors = extraction.split(",")
        for color in colors:
            n, c = color.strip().split(" ")
            n = int(n)
            if(n != 0 and n > colours_min[c]):
                colours_min[c] = n
    
    return True, colours_min

games = read_file_lines("day2.txt")

#1
result = 0
for i, game in enumerate(games):
    winning = parse_game(game)
    if winning:
        result += i+1
print(result)

#2
result = 0
for i, game in enumerate(games):
    winning, colours = parse_game_min_colors(game)
    if winning:
        result += math.prod(colours.values())
print(result)