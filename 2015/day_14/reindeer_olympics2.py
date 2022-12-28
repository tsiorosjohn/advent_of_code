import itertools
import re
from pprint import pprint
from string import ascii_lowercase
# CLOCK_CYCLES = 1000
CLOCK_CYCLES = 2503

def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def get_speed_rest(ls):
    names_f = []
    speed_rest_f = {}
    for item in ls:
        print('=======', item)
        names_f.append(item.split()[0])
        speed_rest_f[item.split()[0]] = (int(item.split()[3]), int(item.split()[6]), int(item.split()[13]))  # speed / speed-duration / rest-duration
    names_f = list(set(names_f))
    # print(f"{speed_rest_f = }")
    # print(f"{names = }")
    return names_f, speed_rest_f


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    # print(lines)

    names, speed_rest = get_speed_rest(lines)
    print(names, speed_rest)
    distance = {}
    points = {}
    speed_temp_duration = {}
    rest_temp_duration = {}
    for clock in range(CLOCK_CYCLES):
        for reindeer in names:
            print(f"======== {clock = } / {reindeer} / {speed_temp_duration = } / {rest_temp_duration = } ========")
            # initialize in first clock cycle
            if clock == 0:
                speed_temp_duration[reindeer] = speed_rest[reindeer][1]  # first run, initialize to correct speed
                rest_temp_duration[reindeer] = speed_rest[reindeer][2]
                distance[reindeer] = 0
                points[reindeer] = 0
            if speed_temp_duration[reindeer] > 0:
                distance[reindeer] += speed_rest[reindeer][0]
                speed_temp_duration[reindeer] -= 1
            elif speed_temp_duration[reindeer] == 0:
                rest_temp_duration[reindeer] -= 1
            if rest_temp_duration[reindeer] == 0:
                print(f"rest duration reached to 0. Re-initializing speed & test duration to initial values")
                speed_temp_duration[reindeer] = speed_rest[reindeer][1]
                rest_temp_duration[reindeer] = speed_rest[reindeer][2]
        temp_max_distance = distance[max(distance, key=distance.get)]
        temp_leader_reindeer_ls = [k for k, v in distance.items() if v == temp_max_distance]
        if len(temp_leader_reindeer_ls) > 1:
            print(f"reached!!! {temp_leader_reindeer_ls = }")
        for temp_leader in temp_leader_reindeer_ls:
            points[temp_leader] += 1
            print(f"{temp_leader_reindeer_ls = } // {temp_leader = }")
            print(f'Results for: {clock = }: {distance = } \n'
                  f'{distance[max(distance, key=distance.get)]} for reindeer: {temp_leader = }', f"{points = }")

    print('\nfinal stats: ', distance, f"\n{points = }, \n"
                                       f"max points: {points[max(points, key=points.get)]} for reindeer: {max(points, key=distance.get)}")
    print(f'\nmax distance: {distance[max(distance, key=distance.get)]} for reindeer: ', max(distance, key=distance.get))

