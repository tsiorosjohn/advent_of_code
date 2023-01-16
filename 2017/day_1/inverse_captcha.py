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
    for i in range(len(string)):
        if i == len(string) - 1:
            # print(f"{string[i] = }")
            if string[i] == string[0]:
                sum += int(string[0])
            break
        if string[i] == string[i + 1]:
            sum += int(string[i])
    print(f"{sum = }")


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    for line in lines:
        print(f"\n================ {line = } ================")
        find_sum(line)
