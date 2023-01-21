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

    max_reg_value = 0
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
        # print(max(registers.items(), key=lambda item: item[1]))
        print(f"value of {reg = } is {registers[reg]}")
        print(f"{registers = }")
        if registers[reg] > max_reg_value:
            max_reg_value = registers[reg]

    print(registers)
    print(max(registers.values()))
    print(max(registers.items(), key=lambda item: item[1]))
    print(f"Max value ever was: {max_reg_value = }")