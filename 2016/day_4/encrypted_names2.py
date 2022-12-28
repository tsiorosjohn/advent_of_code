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
    # encrypted_name = encrypted_name.replace('-', '')
    sorted_by_count = sorted(Counter(encrypted_name.replace('-', '')).most_common(),
                             key=lambda tup: (-tup[1], tup[0]))  # first sort by count reversed / second sort by alphabetical order
    # print(sorted_by_count)
    get_top_five = ''.join([item[0] for item in sorted_by_count])[:5]
    # print(f"{get_top_five = }")
    if get_top_five == checksum:
        print(f"{get_top_five = } matches {checksum = } !!!!")
        valid_rooms.append((encrypted_name, sector_id))
        return sector_id
    else:
        print(f"{get_top_five = } of decoy")
        return 0


def decrypt_room(room, s_id):
    """To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID.
    A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces."""

    def next_alpha(s):
        return chr((ord(s) + 1 - 97) % 26 + 97)  # ord('a') = 97

    def next_nth_alpha(s, n):
        """return nth next character"""
        return chr((ord(s) + n - 97) % 26 + 97)  # ord('a') = 97

    decrypted_room = ''
    for char in room:
        if char == '-':  # replace '-' with ' '
            decrypted_room += ' '
        else:
            decrypted_room += next_nth_alpha(char, s_id)
    return decrypted_room


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example2.txt'
    lines = parse_input(file)
    print(lines)
    valid_sector_id_sum = 0
    valid_rooms = []
    for line in lines:
        encrypted_name = re.search(r'(.*)-[0-9]{3}', line).group(1)
        sector_id = int(re.search(r'-([0-9]{3})', line).group(1))
        checksum = re.search(r'\[([a-z]{5})]', line).group(1)
        # print(encrypted_name, sector_id, checksum)

        valid_sector_id = real_room(encrypted_name, sector_id, checksum)
        valid_sector_id_sum += valid_sector_id
    print(f"{valid_sector_id_sum = }")
    print(f"{valid_rooms = }")

    for room, s_id in valid_rooms:
        decrypted_room = decrypt_room(room, s_id)
        # print(room, s_id, '======> ', decrypted_room)
        if 'north' in decrypted_room:
            print(f"North pole relevant decrypted room = {decrypted_room}, with {s_id = }")
