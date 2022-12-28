from pprint import pprint

def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def lights_grid(instructions_ls):
    rows, cols = (1000, 1000)
    # rows, cols = (10, 10)
    grid = [[0 for i in range(cols)] for j in range(rows)]

    def get_coordinate(text, pos=2):
        coordinates = text.split()[pos].split(',')
        return coordinates

    def lights_switch(operation, start, end):
        for row in range(int(end[0]) - (int(start[0])-1)):
            # print(f"row: {row}")
            for col in range(int(end[1]) - (int(start[1])-1)):
                # print(f"   col: {col}")
                if operation == 'on':
                    # print('oper on')
                    grid[int(start[0])+row][int(start[1])+col] += 1
                elif operation == 'off':
                    if grid[int(start[0])+row][int(start[1])+col] == 0:
                        # grid[int(start[0]) + row][int(start[1]) + col] = 0
                        continue
                    else:
                        grid[int(start[0])+row][int(start[1])+col] -= 1
                    # grid[start[0]+row][start[1]+col] = 0
                    # grid[row][col] = 0
                elif operation == 'toggle':
                    # grid[row][col] = (grid[row][col] + 1) % 2
                    # grid[int(start[0]) + row][int(start[1]) + col] = (grid[int(start[0]) + row][int(start[1]) + col] + 1) % 2
                    grid[int(start[0]) + row][int(start[1]) + col] += 2
        return

    for line in instructions_ls:
        if line.startswith('turn on'):
            start = get_coordinate(line, 2)
            end = get_coordinate(line, 4)
            # print(f"turn on: {start, end}")
            lights_switch('on', start, end)
        elif line.startswith('turn off'):
            start = get_coordinate(line, 2)
            end = get_coordinate(line, 4)
            # print(f"turn off: {start, end}")
            lights_switch('off', start, end)
        elif line.startswith('toggle'):
            start = get_coordinate(line, 1)
            end = get_coordinate(line, 3)
            # print(f"toggle: {start, end}")
            lights_switch('toggle', start, end)

    return grid

if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    # file = 'example2.txt'
    # file = 'example_tsio.txt'
    lines = parse_input(file)
    print(lines)

    l_grid = lights_grid(lines)
    # pprint(l_grid)
    sum = 0
    for count, item in enumerate(l_grid):
        for inner in l_grid[count]:
            sum += inner
    print(sum)


