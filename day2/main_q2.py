import re

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            total += power(line)
        return total
    
def test_main():
    with open('test_input.txt', 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            total += power(line)
    return total


def power(line):

    leg = {
        'blue': 0, 
        'red': 0,
        'green': 0,
    }
    matches = re.findall(r'(\d+) (\w+)', line)
    
    for number, color in matches:
        if int(number) > leg[color]:
            leg[color] = int(number)
    product = 1
    for value in leg.values():
        product *= value

    return product