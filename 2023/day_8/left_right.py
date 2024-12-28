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
    # file = 'example2.txt'
    lines = parse_input(file)
    instructions = lines[0]
    print(f"{instructions = } // {lines = }")

    elements_d = {}

    for line in lines[2:]:
        # print(f'\n========== {line = } ================')
        # elements_d[line.split('=')[0].strip()] = line.split('=')[1].strip()[1:-1].split(',')
        elements_d[line.split('=')[0].strip()] = [i.strip() for i in line.split('=')[1].strip()[1:-1].split(',')]
    print(f"{elements_d= }")

    item = 'AAA'
    count = 0
    while True:
        for instruction in instructions:
            print(f"--- {instruction = } --- ")
            if instruction == 'L':
                item = elements_d[item][0]
            elif instruction == 'R':
                item = elements_d[item][1]
            print(f"{item = }")
            count += 1
        if item == 'ZZZ':
            break

    print(f"Finished! {count = }")

