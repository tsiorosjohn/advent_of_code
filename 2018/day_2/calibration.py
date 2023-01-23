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
    double_count = 0
    triple_count = 0

    for line in lines:
        print(f"\n============= {line = } ==============")
        counts = Counter(line)
        print(f"{counts = }")
        double_found = [k for k, v in counts.items() if v == 2]
        triple_found = [k for k, v in counts.items() if v == 3]
        if len(double_found) > 0:
            double_count += 1
        if len(triple_found) > 0:
            triple_count += 1
        # print(f"{double_found = } // {triple_found = }")

    print(f"{double_count = } * {triple_count = } // sum = {double_count * triple_count}")