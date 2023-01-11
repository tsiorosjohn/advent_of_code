import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def decompress_input(text):
    # find_all = re.finditer(r'\(\dx\d\)', text)
    decompressed_str = ''
    multiplier = 1
    while search_marker := re.search(r'\(\d+x\d+\)', text):
        print(f"\n===> {text = }")
        if search_marker:
            print(f"=== {search_marker.string} // {search_marker} ====")
            char_nr = int(search_marker.group()[1:-1].split('x')[0])
            char_repeat = int(search_marker.group()[1:-1].split('x')[1])
            chars_to_repeat = text[search_marker.span()[1]:search_marker.span()[1] + char_nr]
            # first part of the string:
            decompressed_str += text[:search_marker.span()[0]]
            # multiple part of the string:
            chars_to_repeat_sub = chars_to_repeat
            while search_marker_subpart := re.search(r'\(\d+x\d+\)', chars_to_repeat_sub):
                char_repeat_subpart = int(search_marker_subpart.group()[1:-1].split('x')[1])
                multiplier = multiplier * char_repeat_subpart
                chars_to_repeat_sub = chars_to_repeat_sub[search_marker_subpart.span()[1] + char_nr:]

            # decompressed_str += chars_to_repeat * char_repeat
            decompressed_str += chars_to_repeat * multiplier
            multiplier *= char_repeat
            # decompressed_str += text[search_marker.span()[1]+char_nr:]
            print(f"{char_nr = }, {char_repeat = }, {chars_to_repeat_sub = }, {multiplier = } , {search_marker.span()[1] = }, {chars_to_repeat = }")
            print(f"    partly: {decompressed_str = }")
            text = text[search_marker.span()[1] + char_nr:]
        else:
            decompressed_str += text
    else:
        decompressed_str += text
    print(f"{len(decompressed_str) = }")

    decompressed_str = decompressed_str.strip()
    print(f"{decompressed_str = }")
    return decompressed_str


if __name__ == "__main__":
    # file = 'input.txt'
    file = 'example2.txt'
    lines = parse_input(file)
    print(lines)
    for line in lines:
        if line.startswith('#'):
            continue
        # print('=======================')
        sequences = decompress_input(line)
        print(f"{len(sequences) = }")
