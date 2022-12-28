import copy
import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def get_replacements(lines_f):
    """get lines list and create a dict of key-values(lists)"""
    replacements_f = {}
    for line in lines_f:
        field = line.split()
        if field[0] not in replacements_f:
            replacements_f[field[0]] = [field[2]]
        else:
            replacements_f[field[0]] = replacements_f[field[0]] + [field[2]]

    return replacements_f


def molecule_replacements(repl_d, molec):
    """get replacements for a molecule"""
    molec_replac_ls_f = []
    for replac in repl_d:
        for count, replac_item in enumerate(repl_d[replac]):
        #     replac_item = ''
        #     print(f"====== {replac = } // {replac_item = }  - {repl_d[replac] = } // {len(repl_d[replac]) = } ========")
            molecule_combination = ''
            # if replace_elements := re.sub(f'{replac}', replac_item, molec):
            if replace_elements := re.finditer(f'{replac}', molec):
                # print(f"{replac = } - {replace_elements = }")
                for repl_item in replace_elements:
                    print(f"{repl_item = } - {repl_item.group().replace(repl_item.group(), replac_item) = } ")
                    print(f"-----> {molec[:repl_item.start()] + 'xxx' + repl_item.group().replace(repl_item.group(), replac_item) + 'yyy'+ molec[repl_item.start()+1:]}")
                    temp_replac_item = f"{molec[:repl_item.start()] + repl_item.group().replace(repl_item.group(), replac_item) + molec[repl_item.start()+1:]}"
                    # molecule_combination += temp_replac_item
                    molec_replac_ls_f.append(temp_replac_item)
                    # for count in range(len(found_elements)):
                        # print(f'====== {found_elements=} {item_ls=} {len(item_ls)=}  {count=}')
    print(f"{molec_replac_ls_f = }")
    print(f"{set(molec_replac_ls_f) = } - length: {len(set(molec_replac_ls_f))}")
    return molec_replac_ls_f


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    # file = 'example2.txt'
    lines = parse_input(file)

    # get all lines in list from input
    print(lines, len(lines))
    molecule = lines.pop()
    lines.pop()
    print(lines, ',length:', len(lines), f"// {molecule = }")

    replacements = get_replacements(lines)
    print(f"{replacements = }")
    molec_replac_ls = molecule_replacements(replacements, molecule)

