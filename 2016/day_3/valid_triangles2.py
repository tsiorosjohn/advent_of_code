from pprint import pprint


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
    # file = 'example2.txt'
    lines = parse_input(file)
    print(lines)
    valid = 0
    # triangles are specified in groups of three vertically. Each set of three numbers
    # in a column specifies a triangle. Rows are unrelated.
    triangles = {}
    temp_count = 1
    for count, line in enumerate(lines):
        field = line.split()
        # triangles.update([count[field[0]]])
        if (count + 1) % 3 == 1:
            triangles.update({(count + 1) // 3: [field[0]]})
            triangles.update({str((count + 1) // 3) + 'a': [field[1]]})
            triangles.update({str((count + 1) // 3) + 'b': [field[2]]})
            # print(f"{triangles = }")
        elif (count + 1) % 3 == 2:
            triangles[(count + 1) // 3] = triangles[(count + 1) // 3] + [f"{field[0]}"]
            triangles[str((count + 1) // 3) + 'a'] = triangles[str((count + 1) // 3) + 'a'] + [f"{field[1]}"]
            triangles[str((count + 1) // 3) + 'b'] = triangles[str((count + 1) // 3) + 'b'] + [f"{field[2]}"]
        elif (count + 1) % 3 == 0:
            triangles[(count // 3)] = triangles[count // 3] + [f"{field[0]}"]
            triangles[str((count // 3)) + 'a'] = triangles[str(count // 3) + 'a'] + [f"{field[1]}"]
            triangles[str((count // 3)) + 'b'] = triangles[str(count // 3) + 'b'] + [f"{field[2]}"]

    print()

    for k, v in triangles.items():
        print(v)
        if valid_triangle(v[0], v[1], v[2]):
            valid += 1
    print(f"valid triangles {valid}")
