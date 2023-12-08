import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def find_digigs(word):
    """ find first and last digit and concatenate them"""
    first_digit = (re.search(r'\d', word)).group()
    last_digit = (re.search(r'\d(?=[^\d]*$)', word)).group()
    print(f"{first_digit = } / {last_digit = }")
    return int(str(first_digit) + str(last_digit))


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)
    sum = 0
    for line in lines:
        print('==========================')
        print(line)
        sum += find_digigs(line)
    print(f"{sum = }")