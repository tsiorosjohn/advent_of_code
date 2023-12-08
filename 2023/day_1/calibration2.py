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


def replace_word_with_digit(word):
    word = word.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five",
                                                                                                                                         "five5five").replace(
        "six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")
    return word


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example2.txt'
    lines = parse_input(file)
    print(lines)
    sum = 0
    for line in lines:
        print('==========================')
        print(line)
        print(replace_word_with_digit(line))
        sum += find_digigs(replace_word_with_digit(line))
    print(f"{sum = }")
