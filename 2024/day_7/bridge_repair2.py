from itertools import product


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def apply_operations(elements, operations):
    """
    Apply the operations (+, *) between the elements.
    """
    result = elements[0]
    expression = str(elements[0])  # For readable expressions

    for i, op in enumerate(operations):
        if op == '+':
            result += elements[i + 1]
        elif op == '*':
            result *= elements[i + 1]
        elif op == ' ':
            result = int(str(result) + str(elements[i + 1]))  # concatenate two integers and convert to int

        expression += f" {op} {elements[i + 1]}"

    return result, expression


def generate_combinations(elements):
    """
    Generate all combinations of addition and multiplication for a list of integers.
    """
    n = len(elements)
    if n < 2:
        return [elements[0]]

    # Generate all possible operations combinations
    possible_operations = list(product(['+', '*', ' '], repeat=n - 1))
    # print(f"{possible_operations = }")
    results = []

    for operations in possible_operations:
        result, expression = apply_operations(elements, operations)
        results.append((result, expression))

    return results


def check_result(line_f):
    ls_result = int(line_f.split(':')[0])
    elements = [int(item) for item in line_f.split(':')[1].strip().split()]
    # print(f"{ls_result = }, {elements = }")
    combinations = generate_combinations(elements)
    # combinations_no_space = [item[1].replace(' ', '') for item in combinations]
    combinations_no_space = [(value, item.replace(" ", "")) for value, item in combinations]

    # print(f"{combinations = } // {combinations_no_space = }")
    # print(f"{combinations = } ")
    # for result, expression in combinations:
    for result, expression in combinations_no_space:
        # print(f"xxxxxxxxxxx: {expression} = {result} // {ls_result = } , {result = }")
        if ls_result == int(result):
            return result
    return 0


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example2.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)
    summary = 0
    for line in lines:
        print('==========================')
        print(line)
        summary += check_result(line)
    print(f"{summary = }")
