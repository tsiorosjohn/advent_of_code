import re


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
    jump_offsets = parse_input(file)
    jump_offsets = [int(jump) for jump in jump_offsets]
    print(jump_offsets)

    steps = 0
    pointer = 0
    while True:
        # for jump in jump_offsets:
        # print(f"\n================ {jump_offsets = } // {steps = } // {pointer = } ================")
        steps += 1
        temp_pointer = pointer
        pointer = jump_offsets[pointer] + temp_pointer
        jump_offsets[temp_pointer] += 1
        print(f"\n================ {jump_offsets = } // {steps = } // {pointer = } // {temp_pointer = } ================")
        if pointer >= len(jump_offsets):
            break


    print(f"{steps = }")
