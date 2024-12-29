def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def safe_check(ls_f, tolerate=False):
    print(f"{ls_f = }")

    def is_safe(ls_inner_f):
        sorted_ls = sorted(ls_inner_f)
        sorted_reverse_ls = sorted(ls_inner_f, reverse=True)
        # check if the adjacent items within the list differ by at least one and at most three:
        for i_f in range(len(ls_inner_f) - 1):
            if abs(ls_inner_f[i_f] - ls_inner_f[i_f + 1]) > 3:
                return 0
            elif abs(ls_inner_f[i_f] - ls_inner_f[i_f + 1]) == 0:
                return 0

        # check ascending/descending of lists:
        if ls_inner_f == sorted_ls or ls_inner_f == sorted_reverse_ls:
            print(f"{ls_inner_f = }, {sorted_ls = }, {sorted_reverse_ls = }")
            return 1
        else:
            return 0

    if not tolerate:
        return is_safe(ls_f)

    # toleration
    elif tolerate:
        for i in range(len(ls_f)):
            modified_report = ls_f[:i] + ls_f[i + 1:]  # Remove the i-th level.
            print(f"{modified_report = }")
            if is_safe(modified_report):
                print(f"{is_safe(modified_report) = }")
                return 1
        else:
            return 0


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)
    safe_reports_summary = 0
    safe_reports_tolerate_summary = 0
    for line in lines:
        print('==========================')
        print(line)
        safe_reports_summary += safe_check([int(item) for item in line.split()])
        safe_reports_tolerate_summary += safe_check([int(item) for item in line.split()], tolerate=True)
    print(f"{safe_reports_summary = }, {safe_reports_tolerate_summary = }")
