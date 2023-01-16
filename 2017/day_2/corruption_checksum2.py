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

    total = 0
    for line in lines:
        line_ls = line.split()
        line_ls_int = [int(x) for x in line_ls]
        print(f"\n================ {line_ls = } // {line_ls_int = }================")
        for i, item in enumerate(line_ls_int):
            for j in range(len(line_ls_int)):
                if i == j:
                    continue
                if line_ls_int[i] % line_ls_int[j] == 0:
                    division = int(line_ls_int[i] / line_ls_int[j])
                    print(f"{division = }")
                    total += division

    print(f"{total = }")
