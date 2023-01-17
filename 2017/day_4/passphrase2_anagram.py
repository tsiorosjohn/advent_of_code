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
    # file = 'example2.txt'
    lines = parse_input(file)
    print(lines)

    total_valid = 0
    for line in lines:
        line_ls = line.split()
        sorted_ls = [''.join(sorted(item, key=str.lower)) for item in line_ls]
        print(f"\n================ {line_ls = } // {sorted_ls = }================")

        if len(set(sorted_ls)) == len(sorted_ls):
            print(f"valid")
            total_valid += 1
    print(f"{total_valid = }")