import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        # for item in flines:
            # input_ls.append(item.rstrip())
            # input_ls.append(item.replace('\n', ''))  # remove new line characters
            # Join all lines into a single string and remove newline characters
        input_ls = [''.join([item.strip() for item in flines])]

    return input_ls


def match_pattern(text):
    # Regex pattern
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Find all matches
    matches = re.findall(pattern, text)

    # Print results
    print(matches)

    summary = 0
    for tuple in matches:
        print(tuple)
        print(int(tuple[0]) * int(tuple[1]))
        summary += int(tuple[0]) * int(tuple[1])
    return summary

    # get input text with while and search for pattern 'do()' or don't() if found, delete text in between don't() and do()


def recreate_input(line_f):
    while True:
        # Regex pattern to find text between don't() and do()
        pattern = r"don't\(\).*?do\(\)"

        # Search for the pattern
        match = re.search(pattern, line_f)

        if not match:
            break

        # Remove the found pattern
        line_f = re.sub(pattern, '', line_f, )

    return line_f


if __name__ == "__main__":
    # file = 'example.txt'
    # file = 'input_one_line.txt'
    file = 'input.txt'
    # file = 'example2.txt'
    lines = parse_input(file)
    print(lines)
    mul_summary = 0
    mul_summary2 = 0
    for line in lines:
        print('==========================')
        print(line)
        mul_summary += match_pattern(line)
        mul_summary2 += match_pattern(recreate_input(line))
    print(f"{mul_summary = }, {mul_summary2 = }, {len(lines) = }")
