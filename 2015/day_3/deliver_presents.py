def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def get_houses(ls):
    """get houses that receive at least one present"""
    x = 0
    y = 0
    grid = [(0, 0)]
    for house in ls:
        if house == '>':
            x += 1
        elif house == '<':
            x -= 1
        elif house == '^':
            y += 1
        elif house == 'v':
            y -= 1
        grid.append((x, y))
    return grid


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    for house in lines:
        grid1 = get_houses(house)
        print(grid1)
        print(set(grid1))  # remove houses that were visited twice
        print(len(set(grid1)))

