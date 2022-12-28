

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
    print(expanded_list1)
    print(expanded_list2)

    # check if list1 is fully contained in list2:
    included_items_nr = 0
    equal_items_nr = 0
    for count, item in enumerate(expanded_list1):
        print(f"{item=} - {expanded_list2[count]=}")

        # we should subtract the "equal" items, as those are calculated twice!!!
        if item == expanded_list2[count]:
            print('EEEEEEQUAL')
            equal_items_nr += 1
        if set(item).issubset(expanded_list2[count]):
            print(f"INCLUDED ITEM:{item = }")
            included_items_nr += 1

    # count vice versa as well
    for count, item in enumerate(expanded_list2):
        print(f"{item=} - {expanded_list1[count]=}")
        if set(item).issubset(expanded_list1[count]):
            print(f"INCLUDED ITEM:{item = }")
            included_items_nr += 1

    print(included_items_nr-equal_items_nr)
