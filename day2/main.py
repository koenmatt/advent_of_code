import re

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            total += is_possible(line)
        return total
def test_main():
    with open('test_input.txt', 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            total += is_possible(line)
    return total


legend = {
    'blue': 14,
    'red': 12,
    'green': 13
}


def is_possible(line):

    game_number = re.search(r'Game (\d+):', line).group(1)
    matches = re.findall(r'(\d+) (\w+)', line)
    
    for match in matches:
        if int(match[0]) > legend[match[1]]:
            return 0
    return int(game_number)

