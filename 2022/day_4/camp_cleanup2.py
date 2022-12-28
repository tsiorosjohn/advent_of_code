

def parse_input(file):
    with open(file) as reader:
        lines = reader.readlines()
    return lines


def expand_section(section_range):
    expanded = []
    # print(f"{section_range=}")
    first = section_range.split('-')[0]
    second = section_range.split('-')[1]
    # print(f'=== {first=}, {second=}')
    for count, item in enumerate(range(int(second) - int(first)+1)):
        expanded.append(int(first) + count)
    return expanded


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'

    lines = parse_input(file)
    print(lines)

    summary = 0
    expanded_list1 = []
    expanded_list2 = []
    for line in lines:
        line = line.strip()
        # print(f"{line.split(',')[0] = }")
        # print(f"{line.split(',')[1] = }")
        expanded_list1.append(expand_section(line.split(',')[0]))
        expanded_list2.append(expand_section(line.split(',')[1]))
    # print(expanded_list1)
    # print(expanded_list2)

    # check if list1 is fully contained in list2:
    included_items_nr = 0
    overlap_sections = 0
    equal_items_nr = 0
    for count, item in enumerate(expanded_list1):
        print(f"{item=} - {expanded_list2[count]=}")
        for element in item:
            if element in expanded_list2[count]:
                overlap_sections += 1
                print(f"{item=}")
                break

    print(f"{overlap_sections=}")
    # print(included_items_nr-equal_items_nr)
