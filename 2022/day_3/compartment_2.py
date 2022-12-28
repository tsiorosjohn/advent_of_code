from string import ascii_lowercase as alc
from string import ascii_uppercase as auc
from pprint import pprint


def parse_input(file):
    with open(file) as reader:
        lines = reader.readlines()
    return lines


def find_item_in_both(first, second):
    for item in first:
        if item in second:
            return item


def assign_value_to_letter():
    letter_values = {}
    for value, letter in enumerate(alc, start=1):
        # print(value, letter)
        letter_values[letter] = value
    for value, letter in enumerate(auc, start=27):
        # print(value, letter)
        letter_values[letter] = value
    return letter_values


def split_in_groups_of_three(lines_list):
    split_list = []
    for i in range(0, len(lines_list), 3):
        split_list.append([lines_list[i].strip(), lines_list[i+1].strip(), lines_list[i+2].strip()])
    return split_list


def find_badge(first, second, third):
    for letter in first:
        if letter in second and letter in third:
            return letter


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example2.txt'

    lines = parse_input(file)
    # print(lines)

    dict_letter_value = assign_value_to_letter()
    # print(dict_letter_value)

    summary = 0
    for line in lines:
        line = line.strip()
        half_line = int(len(line)/2)
        first = line[:half_line]
        second = line[half_line:]
        # print(f"{line=}, {len(line)=} / {half_line=} - {line[:half_line]} - {line[half_line:]}")
        item = find_item_in_both(first, second)
        summary += dict_letter_value[item]
        # print(item)
    print(f"{summary = }")

    split_list = split_in_groups_of_three(lines)
    pprint(split_list)

    summary_part2 = 0
    for group in split_list:
        # for item in group:
        badge = find_badge(group[0], group[1], group[2])
        print(badge)
        summary_part2 += dict_letter_value[badge]
    print(summary_part2)
