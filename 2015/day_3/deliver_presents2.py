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
    xr = 0
    yr = 0
    grid_santa = [(0, 0)]
    grid_robo_santa = [(0, 0)]
    for count, house in enumerate(ls):
        if count % 2 == 0:
            if house == '>':
                x += 1
            elif house == '<':
                x -= 1
            elif house == '^':
                y += 1
            elif house == 'v':
                y -= 1
            grid_santa.append((x, y))

        else:
            if count % 2 == 1:
                if house == '>':
                    xr += 1
                elif house == '<':
                    xr -= 1
                elif house == '^':
                    yr += 1
                elif house == 'v':
                    yr -= 1
            grid_robo_santa.append((xr, yr))
    grid_santa_set = set(grid_santa)
    grid_robo_santa_set = set(grid_robo_santa)
    full_grid = list(grid_santa_set) + list(grid_robo_santa_set)
    return set(full_grid)


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example2.txt'
    lines = parse_input(file)
    print(lines)

    for house in lines:
        full_grid1 = get_houses(house)
        print(full_grid1)
        print(len(full_grid1))

