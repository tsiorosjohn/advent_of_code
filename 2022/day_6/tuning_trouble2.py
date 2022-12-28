
def parse_input(file1):
    with open(file1) as reader:
        flines = reader.readlines()
    return flines


def find_marker(text):
    """find start-of-packet marker based on if they are 4 subsequent characters"""
    # position = 0
    print(f"{text=}")
    for position, i in enumerate(range(len(text)-4)):
        # print(text[i], text[i+1:i+4])
        if len(text[i:i+14]) == len(set(text[i:i+14])):
            print(f"marker found in position {i}: {text[i:i+4]}")
            # position = i
        # else:
        #     print('else')
            return position+14


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example2.txt'

    lines = parse_input(file)
    print(lines)

    for pos in lines:
        input = pos.rstrip().split(':')[0]
        # print(f"{input = }")
        position1 = find_marker(input)
        print(f"{position1 = }")

