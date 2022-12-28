import parse

def parse_input(file):
    with open(file) as reader:
        lines = reader.readlines()
    return lines


def create_crates(text_ls):
    """create lists for all crates from input"""
    crates = []
    crates_non_empty = []
    for item in text_ls[::-1]:  # invert. bottom first
        for count, char in enumerate(item):
            crates.append([])
            crates[count].append(char)
    for item in crates:
        # print(f"{item = }")
        if len(item) > 0 and item != [' '] and item != [' ', ' ', ' '] and item != [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']:
            # print(f"item cleaned: {item }")
            crates_non_empty.append(item)
        # for i in item:
        #     # print('')
        #     if i == ' ' or i == '\n' or i == ' ':
        #         item.remove(i)
    # print(f"{crates_non_empty=}")
    cleaned2 = []
    for item in crates_non_empty:
        # for i in item:
            # print('')
            # if i == ' ' or i == '\n' or i == ' ':
            #     item.remove(i)
        item1 = [i for i in item if i != ' ']
        cleaned2.append(item1)
    print(f"{crates_non_empty=}")
    print(f"{cleaned2=}")
    return cleaned2


def get_movements(text):
    movements = parse.search("move {move} from {from} to {to}", text)
    # print(f"{movements = }")
    return movements


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'

    lines = parse_input(file)

    crates_text = []
    moves_all = []
    for line in lines:
        if '[' in line:
            line = line.replace('[', ' ').replace(']', ' ')
            crates_text.append(line.rstrip('\n'))
            continue
        elif 'move' in line:
            moves_all.append(get_movements(line))
            # print(f"{moves_all = }")
        elif len(line) > 1:
            number_of_crates = int(line.rstrip()[-1])

    crates = create_crates(crates_text)
    # print(moves_all)
    # print(crates)

    # for move in moves_all:
        # print(move)

    print(f"\n{crates = }")
    for move in moves_all:
        # print(f"====, {move = }, {crates[int(move['from'])-1] = }, {crates[int(move['to'])-1] = }")
        print(f"{move = }")
        # temp_ls = crates[-int(move['move'])]
        temp_ls = crates[int(move['from'])-1][-int(move['move']):]
        print(f"{temp_ls = } - {int(move['move']) = } - "
              f"{crates[int(move['from'])-1] = } - {crates[int(move['to'])-1] = }")
        crates[int(move['from'])-1] = crates[int(move['from'])-1][:-int(move['move'])]  # remove 'moves' from 'from'
        crates[int(move['to'])-1] = crates[int(move['to'])-1] + temp_ls  # add 'moves' from 'from' to 'to'
        print(f"after movement: {crates = }")

        # for pop_item in range(int(move['move'])):
        #     temp = crates[int(move['from'])-1].pop()
        #     crates[int(move['to'])-1].append(temp)
            # print(f"loop - {crates = }")
            # print(f"{temp = }")
    # print(f"{crates = }")

    top = ''
    # get top of crates:
    for item in crates:
        # print(f"{item[-1] = }")
        top += item[-1]

    print(crates)
    print(f"{top = }")