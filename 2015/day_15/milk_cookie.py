import sys
sys.path.insert(0, '../common')
from general_functions import parse_input


def get_cookie_recipe(ls):
    # ingredients_f = []
    ingredients_d = {}
    for item in ls:
        print('=======', item)
        # ingredients_f.append(item.split()[0])
        ingredients_d[item.split()[0]] = {'capacity': int(item.split()[2][:-1]),
                                          'durability': int(item.split()[4][:-1]),
                                          'flavor': int(item.split()[6][:-1]),
                                          'texture': int(item.split()[8][:-1]),
                                          'calories': int(item.split()[10])}
    print(ingredients_d)
    return ingredients_d


if __name__ == "__main__":
    # file = 'input.txt'
    file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    ingredients = get_cookie_recipe(lines)

    for teaspoon in range(100):
        for ingredient in ingredients:
            print(teaspoon)