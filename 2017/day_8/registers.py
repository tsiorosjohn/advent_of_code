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
    registers = {line.split()[0]: 0 for line in lines}
    print(registers)

    for line in lines:
        line_ls = line.split()
        print(f"\n================ {line_ls = } ================")
        reg, action, value, _, left_operand, operator, right_operand = line_ls[0:7]
        if operator == '>':
            if registers[left_operand] > int(right_operand):
                if action == 'inc':
                    registers[reg] += int(value)
                elif action == 'dec':
                    registers[reg] -= int(value)
        elif operator == '<':
            if registers[left_operand] < int(right_operand):
                if action == 'inc':
                    registers[reg] += int(value)
                elif action == 'dec':
                    registers[reg] -= int(value)
        elif operator == '<=':
            if registers[left_operand] <= int(right_operand):
                if action == 'inc':
                    registers[reg] += int(value)
                elif action == 'dec':
                    registers[reg] -= int(value)
        elif operator == '>=':
            if registers[left_operand] >= int(right_operand):
                if action == 'inc':
                    registers[reg] += int(value)
                elif action == 'dec':
                    registers[reg] -= int(value)
        elif operator == '==':
            if registers[left_operand] == int(right_operand):
                if action == 'inc':
                    registers[reg] += int(value)
                elif action == 'dec':
                    registers[reg] -= int(value)
        elif operator == '!=':
            if registers[left_operand] != int(right_operand):
                if action == 'inc':
                    registers[reg] += int(value)
                elif action == 'dec':
                    registers[reg] -= int(value)

    print(registers)
    print(max(registers.values()))
    print(max(registers.items(), key=lambda item: item[1]))
