import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def find_sum(string):
    sum = 0
    length = len(string)
    halfway = int(length / 2)
    for i in range(length):
        if string[i] == string[(i + halfway) % length]:
            sum += int(string[i])
    print(f"{sum = }")


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example2.txt'
    lines = parse_input(file)
    print(lines)

    for line in lines:
        print(f"\n================ {line = } ================")
        find_sum(line)
