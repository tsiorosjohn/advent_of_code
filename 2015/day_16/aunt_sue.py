from pprint import pprint


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def get_aunt_info(ls):
    aunt_ls = []
    for item in ls:
        print('=======', item)
        aunt_ls.append([
            f"{item.split()[2]} {int(item.split()[3][:-1])}",
            f"{item.split()[4]} {int(item.split()[5][:-1])}",
            f"{item.split()[6]} {int(item.split()[7])}",
            ])

    pprint(aunt_ls)

    return aunt_ls


if __name__ == "__main__":
    file_aunts = 'input.txt'
    file_ticker_tape = 'ticker_tape.txt'
    aunts = parse_input(file_aunts)
    ticker_tape = parse_input(file_ticker_tape)
    pprint(aunts)
    print('ticker tape', ticker_tape)

    aunt_info_ls = get_aunt_info(aunts)
    print('hhhh', aunt_info_ls[1])

    for count, aunt in enumerate(aunt_info_ls):
        # print(count, aunt)
        if set(aunt).issubset(set(ticker_tape)):
            print(f"FOUNDDDD: {aunt = }, {count+1 = }")
