import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def check_pair(string):
    """An ABBA is any four-character sequence which consists of
     a pair of two different characters followed by the reverse of that pair, such as xyyx or abba."""
    # for count, char in enumerate(string):
    valid_abba = ''
    for i in range(len(string) - 3):
        # print(f"{i = }, {string[i] = } {string[i+2] = }")
        if (string[i] == string[i + 3]) and (string[i + 1] == string[i + 2]) and (string[i] != string[i + 1]):
            print(f"=====> valid IP found: {string[i:i + 4]}")
            valid_abba = string[i:i + 4]
    # print(f"{len(valid_abba) = }")
    if len(valid_abba) > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)
    valid_ips = 0
    for line in lines:
        print('=======================')
        hypernet = re.search(r'\[(.+)]', line).group(1)
        hypernet_all = re.findall(r'\[(.+?)]', line)
        ip_start = re.search(r'(.*)\[', line).group(1)
        ip_end = re.search(r'](.*)', line).group(1)
        # ip_all = re.findall(r'^(.+?)\[', line)
        ip_all = re.findall(r'^(.+?)\[|](.+?)\[|](.+)', line)
        ip_all2 = [list(filter(bool, item))[0] for item in ip_all]  # remove empty '' strings from results!!!
        print(ip_start, hypernet, ip_end, f"\n{line = } \n {hypernet_all = } \n"
                                          f"{ip_all = }, \n {ip_all2 = }")

        # check if there is any item in ip_all2 list that it's true...while in parallel there is NOT any element in hyper list!!
        if any([check_pair(item) for item in ip_all2]) and not any([check_pair(item) for item in hypernet_all]):
            valid_ips += 1

    print(f"{valid_ips = }")
