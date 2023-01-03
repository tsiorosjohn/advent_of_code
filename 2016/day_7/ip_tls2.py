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


def ssl_pair(string):
    valid_aba = ''
    valid_abas = []
    for i in range(len(string) - 2):
        # print(f"{i = }, {string[i] = } {string[i+2] = }")
        if string[i] == string[i + 2]:
            print(f"=====> valid ABA found: {string[i:i + 3]}")
            valid_aba = string[i:i + 3]
            valid_abas.append(valid_aba)
    # print(f"{len(valid_abba) = }")
    if len(valid_abas) > 0:
        return True, valid_abas
    else:
        return False, valid_abas


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example2.txt'
    lines = parse_input(file)
    print(lines)
    valid_ips = 0
    valid_ssls = 0
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

        # if any([ssl_pair(item) for item in ip_all2]) and any([check_pair(item) for item in hypernet_all]):
        possible_abas_all_ips = []
        for item in ip_all2:
            possible_abas_all_ips += ssl_pair(item)[1]

        # check BAB from above list of ABAs:
        for aba in possible_abas_all_ips:
            bab = aba[1] + aba[0] + aba[1]
            print(f"{aba = } // {bab = }")
            if any(bab in item for item in hypernet_all):
                print(f"found ssl:{bab = }, {hypernet_all = }")
                valid_ssls += 1

                break

        print(f"{possible_abas_all_ips = }")

    print(f"{valid_ips = }")
    print(f"{valid_ssls = }")
