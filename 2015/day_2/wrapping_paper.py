def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


if __name__ == "__main__":
    # file = 'input.txt'
    file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    paper_sum = 0
    for present_nr, line in enumerate(lines):

        l = int(line.split("x")[0])
        w = int(line.split("x")[1])
        h = int(line.split("x")[2])
        wrap_paper = 2*l*w + 2*w*h + 2*h*l
        extra_paper = min(l*w, w*h, h*l)
        print(f"{l=}, {w=}, {h=} // wrap paper = {wrap_paper} // {extra_paper = }")
        paper_sum += wrap_paper + extra_paper

    print(paper_sum)