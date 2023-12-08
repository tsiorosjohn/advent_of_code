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

    total = 0
    for line in lines:
        line_ls = line.split()
        line_ls_int = [int(x) for x in line_ls]
        print(f"\n================ {line_ls = } // {line_ls_int = }================")
        difference = int(max(line_ls_int)) - int(min(line_ls_int))
        print(f"{max(line_ls_int) = } // {min(line_ls_int) = } //// Difference: {difference}")
        total += difference
    print(f"{total = }")
