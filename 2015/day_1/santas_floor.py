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
    lines = parse_input(file)
    print(lines)

    up = lines[0].count('(')
    down = lines[0].count(')')

    print(f"{up=} - {down=} ==> floor: {up-down}")

    ############ part2 ############
    floor = 0
    position = 1
    for char in lines[0]:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            print(position)
        position += 1


