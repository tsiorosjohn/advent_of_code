import itertools
import re
from pprint import pprint


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def get_cities(ls):
    cities = []
    distances = {}
    for item in ls:
        cities.append(item.split()[0])
        cities.append(item.split()[2])
        distances[f"{item.split()[0]}_{item.split()[2]}"] = item.split()[4]
        distances[f"{item.split()[2]}_{item.split()[0]}"] = item.split()[4]
    cities = list(set(cities))
    print(cities)
    print(f"{distances = }")
    return cities, distances


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    cities, distance = get_cities(lines)
    possible_routes = itertools.permutations(cities)

    possible_distances = []
    for count, alt_routes in enumerate(possible_routes):
        dist = 0
        # print(subset)
        for i in range(len(cities)-1):
            dist += int(distance[f"{alt_routes[i]}_{alt_routes[i + 1]}"])
        possible_distances.append(dist)
        print(f"Route: {alt_routes} = {dist=}")

    print(possible_distances)
    print('min', min(possible_distances))
    print('max', max(possible_distances))
