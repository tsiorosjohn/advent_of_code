def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def valid_triangle(a, b, c):
    """In a valid triangle, the sum of any two sides must be larger than the remaining side"""
    a, b, c = int(a), int(b), int(c)
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        print(f"Not a valid triangle: {a = }, {b = }, {c = }")
        return False


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)
    valid = 0
    for line in lines:
        field = line.split()
        if valid_triangle(field[0], field[1], field[2]):
            valid += 1
    print(f"valid triangles {valid}")
