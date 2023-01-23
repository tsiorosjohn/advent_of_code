def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


if __name__ == "__main__":
    # file = 'input.txt'
    file = 'example2.txt'
    lines = parse_input(file)
    print(lines)
    double_count = 0
    triple_count = 0

for line in lines:
    print(f"\n============= {line = } ==============")
    diff = 0
    if line