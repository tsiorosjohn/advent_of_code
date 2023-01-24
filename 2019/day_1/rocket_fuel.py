from collections import Counter


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

    sum = 0
    for line in lines:
        print(f"\n============= {line = } ==============")
        fuel = int(line) // 3 - 2
        sum += fuel
        print(f"{fuel = }")

    print(f"{sum = }")
