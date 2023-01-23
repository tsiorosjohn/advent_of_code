import re


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
    string = parse_input(file)[0]
    print(string)

    reaction = re.search(r'([a-zA-Z])(?!\1)(?i:\1)', string)
    print(f"group: {reaction.group()}")
    while reaction:
        # print(reaction, reaction.start(), reaction.span(), reaction.end())
        reaction_str = string[:reaction.start()] + string[reaction.end():]
        reaction = re.search(r'([a-zA-Z])(?!\1)(?i:\1)', reaction_str)
        string = reaction_str
        # print(reaction_str)
    print(f"length is: {len(reaction_str)}")
