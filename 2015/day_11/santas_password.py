import itertools
import re
from pprint import pprint
from string import ascii_lowercase


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def calc_next(curent_pwd):
    pwd = []
    next_pwd_f = curent_pwd

    def next_char(pwd1, pos):

        def end_reached(pwd1=pwd1, pos=pos):
            if pwd1[pos] == '{':  # '{' next ascii after 'z'
                pwd1 = pwd1[:pos] + (8-pos)*'a'
                pos -= 1
                print(f'z reached, last {pwd1=} continue with next {pos =}...')
            return pwd1, pos

        if pos == 7:
            pwd1 = pwd1[:pos] + chr(ord(pwd1[pos])+1)
            pwd1, pos = end_reached(pwd1, pos)
        elif pos == 6:
            pwd1 = pwd1[:pos] + chr(ord(pwd1[pos])+1) + 'a'
            pwd1, pos = end_reached(pwd1, pos)
        elif pos == 5:
            pwd1 = pwd1[:pos] + chr(ord(pwd1[pos])+1) + 'aa'
            pwd1, pos = end_reached(pwd1, pos)
        elif pos == 4:
            pwd1 = pwd1[:pos] + chr(ord(pwd1[pos])+1) + 'aaa'
            pwd1, pos = end_reached(pwd1, pos)
        elif pos == 3:
            pwd1 = pwd1[:pos] + chr(ord(pwd1[pos])+1) + 'aaaa'
            pwd1, pos = end_reached(pwd1, pos)
        elif pos == 2:
            pwd1 = pwd1[:pos] + chr(ord(pwd1[pos])+1) + 'aaaaa'
            pwd1, pos = end_reached(pwd1, pos)
        elif pos == 1:
            pwd1 = pwd1[:pos] + chr(ord(pwd1[pos])+1) + 'aaaaa'
            pwd1, pos = end_reached(pwd1, pos)
        elif pos == 0:
            pwd1 = pwd1[:pos] + chr(ord(pwd1[pos])+1) + 'aaaaa'
            pwd1, pos = end_reached(pwd1, pos)

        return pwd1, pos

    # create 8 chars available combinations:
    i = 0
    position = 7
    while True:
        i += 1
        next_pwd_f, position = next_char(next_pwd_f, position)
        # next_pwd_f = next_pwd_f[:position] + chr(ord(next_pwd_f[position])+1)
        print(f"{next_pwd_f = }, {position = }")

        if valid_pwd(next_pwd_f):
            break

        if i == 130:
            break
    return next_pwd_f


def valid_pwd(pwd):
    three_chars, two_pairs = False, False
    if 'i' in pwd or 'o' in pwd or 'l' in pwd:
        print(f" i, o or l inside password - NOT valid!!")
        return False

    # must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz
    for char in ascii_lowercase:
        if char+(chr(ord(char)+1))+(chr(ord(char)+2)) in pwd:
            print(f"three sequential letters found: {char+(chr(ord(char)+1))+(chr(ord(char)+2))}")
        three_chars = True

    # must include at least two different, non-overlapping pairs of letters, like aa, bb, or zz
    re_find = re.findall(r'(.)\1', pwd)
    # print(f"{re_find = }, {len(re_find) = }")
    if len(re_find) >= 2:
        two_pairs = True

    if three_chars and two_pairs:
        return True
    else:
        return False


if __name__ == "__main__":
    # file = 'input.txt'
    file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    # lines = ['abcdefgh']
    for count, line in enumerate(lines):
        next_pwd = calc_next(line)
        if count == 0:
            print(f"current pwd: {line} - {next_pwd=}")
            assert next_pwd == 'abcdffaa'
        elif count == 1:
            print(f"current pwd: {line} - {next_pwd=}")
            assert next_pwd == 'ghjaabcc'
