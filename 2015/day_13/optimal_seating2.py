import itertools
import re
from pprint import pprint
from string import ascii_lowercase


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def get_names_happiness(ls):
    names = []
    happiness = {}
    for item in ls:
        print('=======', item)
        names.append(item.split()[0])
        if item.split()[2] == 'gain':
            happiness[f"{item.split()[0]}_{item.split()[10][:-1]}"] = item.split()[3]
        elif item.split()[2] == 'lose':
            happiness[f"{item.split()[0]}_{item.split()[10][:-1]}"] = -int(item.split()[3])
    names = list(set(names))
    print(names)
    print(f"{happiness = }")
    return names, happiness


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    # print(lines)

    # for line in lines:
    names, hapiness = get_names_happiness(lines)
    for name in names:
        hapiness[f"tsio_{name}"] = 0
        hapiness[f"{name}_tsio"] = 0

    names.append('tsio')

    # hapiness
        # re_find = re.findall(r'-?[0-9]+', line)

    possible_seating = itertools.permutations(names)
    hap_list = []
    for seats in possible_seating:
        # print(seats)
        # for i in range(len(seats)):
        hap_sum = 0
        for count, name in enumerate(seats):
            hap = hapiness[name+'_'+seats[(count+1) % len(seats)]]  # count happiness from name-a to name-b
            # print(f"{name=}, {seats[(count+1) % len(seats)]}, {hap = }")
            hap_sum += int(hap)

            hap2 = hapiness[seats[(count+1) % len(seats)]+'_'+name]  # count happiness from name-b to name-a
            # print(f"{seats[(count+1) % len(seats)] =}, {name}, {hap2 = }")
            hap_sum += int(hap2)
        hap_list.append(hap_sum)
        # print(f"{hap_sum = }")
    print(hap_list)
    print(max(hap_list))