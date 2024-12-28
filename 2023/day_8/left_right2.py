import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls



if __name__ == "__main__":
    # file = 'input.txt'
    # file = 'example.txt'
    # file = 'example2.txt'
    file = 'part2_example.txt'

    lines = parse_input(file)
    instructions = lines[0]
    print(f"{instructions = } // {lines = }")

    elements_d = {}

    for line in lines[2:]:
        # print(f'\n========== {line = } ================')
        # elements_d[line.split('=')[0].strip()] = line.split('=')[1].strip()[1:-1].split(',')
        elements_d[line.split('=')[0].strip()] = [i.strip() for i in line.split('=')[1].strip()[1:-1].split(',')]
    print(f"{elements_d= }")

    items_d = {}
    elements_ending_in_A = []
    for k, elem in elements_d:
        if elem[-1] == 'A':
            items_d.append(elem)

    print(f"{elements_ending_in_A = }")

    # item = 'AAA'
    count = 0
    while True:
        for instruction in instructions:
            print(f"--- {instruction = } --- ")
            for i, item in enumerate(elements_ending_in_A):
                if instruction == 'L':
                    items_d[i] = elements_d[item][0]
                elif instruction == 'R':
                    items_d[i] = elements_d[item][1]
                print(f"{items_d = }")
            count += 1
            # Check if all elements end with 'Z'
            all_elements_end_with_z = all(element.endswith('B') for element in items_d.values())

            # If condition is met, break the loop
        if all_elements_end_with_z or count > 2:
            break
    print(f"Finished! {count = }")

