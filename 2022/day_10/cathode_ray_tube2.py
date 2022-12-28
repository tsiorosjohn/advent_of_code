from pprint import pprint


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def create_cycles_list(ls):
    cycles_list = [0]
    x = 1
    for count, instruction in enumerate(ls):
        if instruction.startswith('noop'):
            cycles_list.append(x)
        elif instruction.startswith('addx'):
            # print(f"{int(instruction.split()[1]) =} + {x = } ==> {value = }")
            cycles_list.append(x)
            x = int(instruction.split()[1]) + x
            cycles_list.append(x)
    print(f"{cycles_list = }")
    return cycles_list


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    signal_strengths = create_cycles_list(lines)

    sum = 0
    for sign_str in [20, 60, 100, 140, 180, 220]:
        # (temp := sign_str * signal_strengths[sign_str - 1])
        print(f"{sign_str = } * {signal_strengths[sign_str - 1]} ==> {(temp:= sign_str * signal_strengths[sign_str - 1])}")
        sum += temp
    print(sum)
