import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
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


def recreate_input(line_f):
    pass

if __name__ == "__main__":
    # file = 'input.txt'
    # file = 'example.txt'
    file = 'example2.txt'
    lines = parse_input(file)
    print(lines)
    mul_summary = 0
    for line in lines:
        print('==========================')
        print(line)
        mul_summary += match_pattern(line)
    print(f"{mul_summary = }")
