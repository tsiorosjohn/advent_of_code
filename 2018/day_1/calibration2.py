def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example2.txt'
    lines = parse_input(file)
    # print(lines)
    lines = [int(line) for line in lines]
    past_frequencies = {0}
    current_frequency = 0

    i = 0
    while True:
        line = lines[i % len(lines)]
        # print(f"=========== {line = } ============\n {past_frequencies = }")
        current_frequency += line
        if current_frequency in past_frequencies:
            print(f"Frequency {current_frequency} found twice!!!!")
            break
        past_frequencies.add(current_frequency)
        i += 1
