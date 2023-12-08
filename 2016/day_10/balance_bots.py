import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def create_instructions(text):
    """ create sequential instruction list based from input.txt"""
    """ assign values to bots
        also creates output bins"""
    value_search = re.search(r'value (.+) goes to bot (.+)', text)
    bot_search = re.search(r'bot (.+) gives low to (.+) and high to (.+)', text)
    if value_search:
        print(f"{value_search.group(0) = } // {value_search.group(1) = } // {value_search.group(2) = }")
        if value_search.group(2) not in bots:
            bots[value_search.group(2)] = [value_search.group(1)]
            instructions.append()
    elif bot_search:
        print(f" {bot_search.group(1) = } // {bot_search.group(2) = } // {bot_search.group(3) = }")


if __name__ == "__main__":
    # file = 'input.txt'
    file = 'example.txt'
    lines = parse_input(file)
    print(lines)
    instructions = []
    bots = {}  # dict --> {bot-1: [value-1, value-2]}

    for line in lines:
        print(f"\n================ {line = } ================")
        create_instructions(line)
