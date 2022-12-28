import re
from pprint import pprint


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def calc_chars_of_code(line_f):
    return len(line_f)


def calc_chars_of_memory(line_f):
    # strip left/right double quotes ("):
    # line_f = line_f.rstrip('"').lstrip('"')
    line_f = line_f
    # print(f"=={line_f}==")
    print(f"=================== {line_f}===================")
    subtracted_chars = 0
    all_hex_chars = []
    if '\\' in line_f:
        hex_chars = re.findall(r'\\x..', line_f)
        if hex_chars:
            print(f'hex found: {line_f} - {hex_chars = }')
            for char in hex_chars:
                print(f"hexxxx {char=}")
                all_hex_chars.append(char)
                subtracted_chars = subtracted_chars + 3
        escaped_backslash = re.findall(r'\\\\', line_f)
        if escaped_backslash:
            print(f'escaped backslash found: {line_f} - {escaped_backslash = }')
            # remove hex from list of escaped chars:
            for char in escaped_backslash:
                subtracted_chars += 1
        escaped_quotes = re.findall(r'\\"', line_f)
        if escaped_quotes:
            print(f'eescaped_quotes found: {line_f} - {escaped_quotes = }')
            # remove hex from list of escaped chars:
            for char in escaped_quotes:
                subtracted_chars += 1

            # subtracted_chars -= len(hex_chars)
    mem_chars = calc_chars_of_code(line_f[1:-1]) - subtracted_chars
    print(f"{mem_chars = } //{calc_chars_of_code(line_f[1:-1]) = } -  {subtracted_chars = }")
    return mem_chars, all_hex_chars


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    # file = 'example2.txt'
    lines = parse_input(file)
    print(lines)

    code_sum = 0
    memory_sum = 0
    all_hex_ls = []
    for line in lines:
        code_sum += calc_chars_of_code(line)
        memory_sum += calc_chars_of_memory(line)[0]
        print(calc_chars_of_memory(line)[1])
        all_hex_ls.append(calc_chars_of_memory(line)[1])
    print(f"{code_sum = } - {memory_sum = } = {code_sum - memory_sum }")
    print(f"{all_hex_ls = }")

    final = []
    for count,item in enumerate(all_hex_ls):
        if len(item) != 0:
            # all_hex_ls.pop(count)
            if len(item) >= 1:
                flat = []
                temp = [i.split(',') for i in item]
                for sublist in temp:
                    for i in sublist:
                        flat.append(i)
                        final.append(i)
                    print(f"{flat = }")
            print(item)
    # print(f"{all_hex_ls = }")
    print(f"{final = }")

    for item in final:
        # print(item[2:])
        print(item[2:], bytes.fromhex(item[2:]).decode('latin'))
