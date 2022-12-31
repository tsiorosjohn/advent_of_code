import re
from collections import Counter


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)
    chars_d = {}
    for line in lines:
        for count, char in enumerate(line):
            chars_d[count] = chars_d.get(count, '') + char

    print(chars_d)

    signal = ''
    for k, v in chars_d.items():
        most_common_char = Counter(v).most_common(1)[0][0]
        print(f"{k = }, {v = } // {most_common_char = }")
        signal += most_common_char
    print(f"{signal = }")
