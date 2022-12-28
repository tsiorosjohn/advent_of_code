from pprint import pprint
import json

def parse_input(file1):
    with open(file1) as reader:
        flines = reader.readlines()
    return flines


if __name__ == "__main__":
    # file = 'input.txt'
    file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    file_system = {}
    # file_system = {".type": "d"}
    current_dir = None
    path = []
    for line in lines:
        split_line = line.rstrip().split()
        # print(split_line)

        if split_line[0] == "$":
            if split_line[1] == "cd":
                if split_line[2] == "/":
                    current_dir = file_system
                elif split_line[2] == "..":
                    current_dir = path.pop()
                else:
                    path.append(split_line[2])
                    # print(f"{split_line[2]=}")
                    path.append(current_dir)
                    # print(f"else: {current_dir=}, {path=}")
        elif split_line[0] == "dir":
            current_dir[split_line[1]] = {".type": "d"}
        else:
            print(f"{split_line[0]=}, {split_line[1]=}, {current_dir=}")
            current_dir[split_line[1]] = {".type": "f", ".size": int(split_line[0])}
            # current_dir[split_line[1]] = 'test'
            # print(f"{current_dir[split_line[1]]}")
            ...
    pprint(file_system, indent=2)
    pprint(f"{path=}", indent=2)
    # print(json.dumps(file_system, indent=4))

