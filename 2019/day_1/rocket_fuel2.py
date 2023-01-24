from collections import Counter


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

    def fuel_calc(mass):
        return int(mass) // 3 - 2


    sum = 0
    for mass in lines:
        module_sum = 0
        print(f"\n============= {mass = } ==============")
        while True:
            fuel = fuel_calc(mass)
            print(f"{fuel = }")
            mass = fuel
            if fuel <= 0:
                sum += module_sum
                print(f"{module_sum = }")
                break
            module_sum += fuel

    print(f"{sum = }")
