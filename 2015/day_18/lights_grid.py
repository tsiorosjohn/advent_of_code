from pprint import pprint
import copy

ROWS = 100
COLS = 100
STEPS = 100


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def lights_grid(instructions_ls):
    # grid initialization // adding also an extra row/column in each edge with 0 values !!!
    grid = [[0 for i in range(COLS + 2)] for j in range(ROWS + 2)]
    for row_nr, row in enumerate(instructions_ls):
        for char_nr, char in enumerate(row):
            # print(f"{grid[row_nr][char_nr]= }, {char = }")
            if char == '#':
                grid[row_nr + 1][char_nr + 1] = 1
            elif char == '.':
                grid[row_nr + 1][char_nr + 1] = 0

    # pprint(grid)
    def neighboring_sum(row_nr_f, col_nr):
        neighb_sum_f = sum([grid[row_nr_f - 1][col_nr - 1], grid[row_nr_f - 1][col_nr], grid[row_nr_f - 1][col_nr + 1],
                               grid[row_nr_f][col_nr - 1],                                 grid[row_nr_f][col_nr + 1],
                               grid[row_nr_f + 1][col_nr - 1], grid[row_nr_f + 1][col_nr], grid[row_nr_f + 1][col_nr + 1],
                               ])
        return neighb_sum_f

    # print('initial grid')
    # pprint(grid)
    for step in range(STEPS):
        ######### Deepcopy is needed in order to copy nested lists as well correctly!!!!!!!!!!!!!!!!!!!!!!!!!!!
        temp_grid = copy.deepcopy(grid)  # use a temp grid as lights should be updated all together in the end of step/cycle!!
        # print(f"Grid before {step = }")
        # pprint(grid)
        for row_nr, row in enumerate(grid):
            # print(f'========== {row_nr = } ==============')
            for char_nr, char in enumerate(row):
                if row_nr == 0 or row_nr == len(grid) - 1 or char_nr == 0 or char_nr == len(grid) - 1:
                    continue  # skipping edge cols/rows
                # grid[row_nr][char_nr] = next_light_step(row_nr, char_nr)
                neigb_sum = neighboring_sum(row_nr, char_nr)

                if grid[row_nr][char_nr] == 1 and (neigb_sum == 2 or neigb_sum == 3):
                    # print(f"on with 2/3 neighbors: {row_nr, char_nr }")
                    temp_grid[row_nr][char_nr] = 1
                elif grid[row_nr][char_nr] == 0 and neigb_sum == 3:
                    # print(f"off with 3 neighbors: {row_nr, char_nr }")
                    temp_grid[row_nr][char_nr] = 1
                else:
                    temp_grid[row_nr][char_nr] = 0
        grid = temp_grid
        # print(f"Grid after {step = }")
        # pprint(grid)
    total_sum = sum(sum(grid, []))
    print('sumf of grid: ', total_sum)

    return grid


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    # pprint(lines)

    l_grid = lights_grid(lines)
    # pprint(l_grid)
