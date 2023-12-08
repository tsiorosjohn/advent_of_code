import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def is_valid(password):
    if len(password) != 6 or password.isdigit() != True:
        print("not valid")
        return False
    if not re.search(r'(\d)\1', password):
        print(f"not regex match")
        return False
    if int(password[0]) <= int(password[1]) <= int(password[2]) <= int(password[3]) <= int(password[4]) <= int(password[5]):
        print('sorted')
        return True
    else:
        print('not sorted')
        return False


if __name__ == "__main__":
    # file = 'input.txt'
    file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    sum = 0
    for line in lines:
        print(f"\n============= {line = } ==============")
        is_valid(line)

    valid_pwds = 0
    for x in range(197487, 673251+1):
        x = str(x)
        if is_valid(x):
            valid_pwds += 1
    print(valid_pwds)