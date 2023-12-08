
def main():
    with open('test_input.txt', 'r') as file:
        lines = file.readlines()
        store_index(lines)


SYMBOLS = ['*', '$', '=', '#', '%', '/', '&', '+', '-', '@']


DIMS = [140, 140]

def store_index(line_array):
    """Stores index of symbol, returing a list of their indices
    
        stores indices in dict for each char in number, with key being number
    """

    total = 0
    for y in range(len(line_array)):
        print(f"Total: {total}")
        prev_symbol = False # did we previously see a symbol
        current_num = []
        num_validated = False
        for x in range(len(line_array[y])):
            if line_array[y][x] == '.':
                if num_validated:
                    total += int("".join(current_num))
                    print(int("".join(current_num)))
                    current_num = []
                num_validated = False
                continue
            elif line_array[y][x] in SYMBOLS:
                num_validated = False
                prev_symbol = True
            elif num_validated:
                current_num.append(line_array[y][x])
            else:
                if prev_symbol:
                    num_validated = True
                    current_num.append(line_array[y][x])
                    continue
                if x < len(line_array[y]) - 1:
                    if line_array[y][x + 1] in SYMBOLS:
                        num_validated = True
                        current_num.append(line_array[y][x])
                        continue
                if y > 0:
                    if line_array[y - 1][x] in SYMBOLS:
                        num_validated = True
                        current_num.append(line_array[y][x])
                        continue
                if y > len(line_array):
                    if line_array[y + 1][x] in SYMBOLS:
                        num_validated = True
                        current_num.append(line_array[y][x])
                        continue

    return total