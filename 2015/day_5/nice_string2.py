import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def nice_string_checker_part2(text):
    nice_flag = False
    # if temp := re.search(r'([a-z])\1', text):  # contains two letters in a row
    if temp := re.search(r'(..).*\1', text):  # contains two letters in a row
        print(text, f'twice in a row for letter {temp}')
        # if temp := re.search(r'[a-z]', text):  #
        if temp := re.search(r'(.).\1', text):  # one letter which repeats with exactly one letter between them
            print(text, f'Repeated with one in the middle {temp}')
            nice_flag = True
    return nice_flag


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example2.txt'
    lines = parse_input(file)
    print(lines)

    sum = 0
    for line in lines:
        print('==================== ', line, ' ==================== ')
        if nice_string_checker_part2(line):
            sum += 1
        print('==>', line, nice_string_checker_part2(line))
    print(f"{sum = }")

