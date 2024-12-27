def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


if __name__ == "__main__":
    l_ls, r_ls = [], []
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)
    summary = 0
    sum_similar = 0
    for line in lines:
        print('==========================')
        print(line)
        l_ls.append(int(line.split()[0]))
        r_ls.append(int(line.split()[1]))
        l_ls.sort()
        r_ls.sort()
        print(f"{l_ls = }, {r_ls = }")
    for i in range(len(l_ls)):
        # tmp = 0
        # tmp_similar = 0
        tmp = abs(l_ls[i] - r_ls[i])
        tmp_similar = r_ls.count(l_ls[i])
        print(f"{tmp = }, {tmp_similar = } // {l_ls[i] = }")
        summary += tmp
        sum_similar += tmp_similar * l_ls[i]
    print(f"{summary = }, {sum_similar = }")
