


##### Question 1. I got the star! ########


def q1_main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        sum = 0
        for line in lines:
            num = int(q_1_extract_numbers(line))
            print(num)
            sum += num
    return sum

            
def q_1_extract_numbers(input_line):
    
    first_num, last_num, curr_index_forward, curr_index_backward = 0, 0, 0, len(input_line) - 1
    is_char_forward, is_char_backward = True, True
    
    while is_char_forward:
        if input_line[curr_index_forward].isdigit():
            first_num = input_line[curr_index_forward]
            is_char_forward = False
        curr_index_forward += 1
    
    
    while is_char_backward:
        if input_line[curr_index_backward].isdigit():
            last_num = input_line[curr_index_backward]
            is_char_backward = False
        curr_index_backward -= 1
    
    return first_num + last_num


############################################################ Question 2 ###############################################################


def q2_extract_numbers(input_line):
    
    first_num, last_num, curr_index_forward, curr_index_backward = 0, 0, 0, len(input_line) - 1
    is_char_forward, is_char_backward = True, True
    
    while is_char_forward:
        if input_line[curr_index_forward].isdigit():
            first_num = input_line[curr_index_forward]
            is_char_forward = False
        curr_index_forward += 1
    
    # print("----Forward-----")
    forward_line = input_line[:curr_index_forward]
    # print(f"forward line: {forward_line}")
    num = extract_words_forward(forward_line)
    if num > 0:
        first_num = str(num)
   

    while is_char_backward:
        
        if input_line[curr_index_backward].isdigit():
            last_num = input_line[curr_index_backward]
            is_char_backward = False
        curr_index_backward -= 1
    
    # print("----Backward-----")
    backward_line = input_line[curr_index_backward + 1:]
    # print(f"backward line: {backward_line}")
    num2 = extract_words_backward(backward_line)
    if num2 > 0:
        last_num = str(num2)
    return first_num + last_num




def extract_words_forward(line):
    number_names = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    current_min = len(line)
    current_val = 0
    for key, value in number_names.items():
        ind = line.find(key)
        if ind >= 0 and ind < current_min:
            current_min = ind
            current_val = value
    return current_val

def extract_words_backward(line):
    number_names = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    current_min = 0
    current_val = 0
    for key, value in number_names.items():
        ind = line.rfind(key)
        if ind >= 0 and ind > current_min:
            current_min = ind
            current_val = value
    return current_val



def q2_main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        sum = 0
        for line in lines:
            print(f"Line: {line}")
            num = int(q2_extract_numbers(line))
            print(num)
            sum += num
    return sum