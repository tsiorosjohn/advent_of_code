import re


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

    total_valid = 0
    for line in lines:
        line_ls = line.split()
        print(f"\n================ {line_ls = } ================")

        if len(set(line_ls)) == len(line_ls):
            print(f"valid")
            total_valid += 1
    print(f"{total_valid = }")