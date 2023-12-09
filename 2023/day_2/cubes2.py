import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def find_max_per_color(line_f):
    """ find max number per color per game"""
    game_id = int(line_f.split(':')[0].split()[1])
    print(f"{game_id = }")
    all_sets = line_f.split(':')[1]
    all_sets_ls = all_sets.split(';')
    print(f"{all_sets_ls = }")
    list_of_mappings = []
    for set in all_sets_ls:
        print(set)
        pattern = r'(\d+)\s+(\w+)'
        matches = re.findall(pattern, set)
        print(f"{matches = }")
        mapping = {color: int(number) for number, color in matches}
        print(f"{mapping = }")
        list_of_mappings.append(mapping)
        print(f"{list_of_mappings = }")

    # find maximum from list of mappings
    max_numbers = {}

    for mapping in list_of_mappings:
        for color, number in mapping.items():
            if color not in max_numbers or number > max_numbers[color]:
                max_numbers[color] = number

    # print(f"{max_numbers = }")
    # check which is valid game? i.e. it has no more than 12 red cubes, 13 green cubes, and 14 blue cubes
    if max_numbers.get('red', 0) <= 12 and max_numbers.get('green', 0) <= 13 and max_numbers.get('blue', 0) <= 14:
        print(f"---> Valid game: {game_id = }")

        return max_numbers, game_id
    else:
        return max_numbers, 0


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)
    sum = 0
    for line in lines:
        set_multiplier = 1
        print('\n==========================')
        print(line)
        max_numbers, game_id = find_max_per_color(line)
        print(f"\n>>> {max_numbers = } !!!\n")
        # multiply items of each set:
        for value in max_numbers.values():
            set_multiplier *= value

        print(f"{set_multiplier = }")
        sum += set_multiplier

    print(f"{sum = }")
