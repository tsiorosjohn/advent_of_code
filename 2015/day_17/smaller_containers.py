import itertools
# LITER_SUMMARY = 25
LITER_SUMMARY = 150


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

    print(lines, len(lines))

    container_combinations = 0
    for i in range(len(lines)+1):
        possible_containers = itertools.combinations(lines, i)
        for containers in possible_containers:
            # print(containers)
            summary = sum([int(item) for item in containers])
            if summary == LITER_SUMMARY:
                print(summary, containers)
                container_combinations += 1
    print(f"{container_combinations = }")
