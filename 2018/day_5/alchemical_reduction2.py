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
    # print(string)

    def get_polymer_length(str_):
        reaction = re.search(r'([a-zA-Z])(?!\1)(?i:\1)', str_)

        # print(f"group: {reaction.group()}")
        while reaction:
            # print(reaction, reaction.start(), reaction.span(), reaction.end())
            reaction_str = str_[:reaction.start()] + str_[reaction.end():]
            reaction = re.search(r'([a-zA-Z])(?!\1)(?i:\1)', reaction_str)
            str_ = reaction_str
            # print(reaction_str)
        # print(f"======> length is: {len(reaction_str)}")
        return len(reaction_str)


    all_chars = re.findall(r'\w', string)
    print(all_chars)
    all_chars = set(all_chars)
    all_chars_lower = {char.lower() for char in all_chars}
    # all_chars = []
    print(f"{all_chars_lower = }")

    length_ls = []
    for char in all_chars_lower:
        reduced_string = string.replace(char, '').replace(char.upper(), '')
        print(f"{char = } // {reduced_string = }")
        length_ls.append(get_polymer_length(reduced_string))

    print(f"{length_ls = }")
    print(min(length_ls))
