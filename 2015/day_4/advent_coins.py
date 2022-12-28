import hashlib


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
    lines = parse_input(file)
    print(lines)

    quiz_part1 = False
    for line in lines:
        part2_count = 1
        while True:
            part2_count += 1
            temp_md5 = hashlib.md5((line+str(part2_count)).encode('utf-8')).hexdigest()
            if quiz_part1:
                if temp_md5.startswith('00000'):
                    print(part2_count)
                    break
            else:
                if temp_md5.startswith('000000'):
                    print(part2_count)
                    break

