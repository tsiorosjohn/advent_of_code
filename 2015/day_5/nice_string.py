import re

def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def nice_string_checker(text):
    nice_flag = False
    if temp := re.search(r'([a-z])\1', text):  # contains two letters in a row
        print(text, f'twice in a row for letter {temp}')
        if temp := re.findall(r'([aeiou])', text):  # contains at least three vowels
            if len(temp) >= 3:
                print(text, f'three vowels: {temp}')
                nice_flag = True
    if any(['ab' in text, 'cd' in text, 'pq' in text, 'xy' in text]):
        print(text, 'disallowed strings')
        nice_flag = False
    return nice_flag


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    sum = 0
    for line in lines:
        if nice_string_checker(line):
            sum += 1
        print('======', line, nice_string_checker(line))
    print(f"{sum = }")