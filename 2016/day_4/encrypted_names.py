import re
from collections import Counter


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def real_room(encrypted_name, sector_id, checksum):
    """A room is real (not a decoy) if the checksum is the five most common
     letters in the encrypted name, in order, with ties broken by alphabetization"""
    encrypted_name = encrypted_name.replace('-', '')
    sorted_by_count = sorted(Counter(encrypted_name).most_common(),
                             key=lambda tup: (-tup[1], tup[0]))  # first sort by count reversed / second sort by alphabetical order
    # print(sorted_by_count)
    get_top_five = ''.join([item[0] for item in sorted_by_count])[:5]
    # print(f"{get_top_five = }")
    # sector_id_sum = 0
    if get_top_five == checksum:
        print(f"{get_top_five = } matches {checksum = } !!!!")
        # sector_id_sum += sector_id
        return sector_id
    else:
        return 0


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)
    valid_sector_id_sum = 0
    for line in lines:
        encrypted_name = re.search(r'(.*)-[0-9]{3}', line).group(1)
        sector_id = int(re.search(r'-([0-9]{3})', line).group(1))
        checksum = re.search(r'\[([a-z]{5})]', line).group(1)
        # print(encrypted_name, sector_id, checksum)

        valid_sector_id = real_room(encrypted_name, sector_id, checksum)
        valid_sector_id_sum += valid_sector_id
    print(f"{valid_sector_id_sum = }")