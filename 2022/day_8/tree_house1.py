from pprint import pprint


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def count_edge(ls):
    edge_nr = len(ls)*4 - 4
    print(f"list length: {len(ls)}")
    return edge_nr


def is_visible(tree_list):
    """create a list of trees without the edge-trees
       subsequently for each tree find if this is the max in row/column
    """
    tree_no_edge = []
    tree_no_edge_temp = tree_list[1:len(tree_list)-1]
    # print(f"temp {tree_no_edge_temp = }")
    tree_no_edge = [tree[1:len(tree)-1] for tree in tree_no_edge_temp]
    print(f"final {tree_no_edge = }")

    visible_count = 0
    # for row_count, row in enumerate(tree_no_edge):
    for row_count, row in enumerate(tree_list):
        if row_count == 0 or row_count == len(tree_list)-1:
            print(f"ROW COUNT skipping...: {row_count} for {len(tree_list) = }")
            continue
        # for col_count, tree in enumerate(row):
        #     if col_count == 0 or col_count == len(tree_list) - 1:
        #         print(f"COL COUNT skipping...: {col_count} for {len(tree_list) = }")
        #         continue
        #     print(f"{row_count = } - {col_count = }, {tree = }")
        #     # find if it's visible in current row:
        if int(tree) is max([int(item) for item in tree_list[row_count]]):
            print(f"{row_count = } - {col_count = }, {tree = } is max inside {tree_list[row_count] = })")
            visible_count += 1
            continue  # break loop in case max it's found
            # visible in column?
    for col_count, tree in enumerate(tree_list):
        if col_count == 0 or col_count == len(tree_list) - 1:
            print(f"COL COUNT skipping...: {col_count} for {len(tree_list) = }")
            continue
        # print(f"{row_count = } - {col_count = }, {tree = }")
        if int(tree) is max([int(item[col_count]) for item in tree_list]):
            print(f"{tree = } is max inside {tree_list[col_count] = }) ===== {[int(item[col_count]) for item in tree_list] = }")
            visible_count += 1
            continue  # break loop in case max it's found

            # if int(tree) > int(tree_list[row_count+1][tree_count]):
            #     print(f"{tree = } is visible (bigger than: {tree_list[row_count+1][tree_count]} from: {tree_list[row_count+1]})")
            #     visible_count += 1

    print(f"{visible_count = }")
    return visible_count


if __name__ == "__main__":
    # file = 'input.txt'
    file = 'example.txt'
    lines = parse_input(file)
    print(lines)
    edge = count_edge(lines)
    print(f"{edge = }")

    count_inside = is_visible(lines)

    print(f"tress= {count_inside=} + {edge=} = {count_inside+edge}")

