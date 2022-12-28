
def get_score(opponent, you):
    """calculate score for each round"""
    round_score = 0
    # get score based on your choise:
    if you == 'A':
        round_score += 1
    elif you == 'B':
        round_score += 2
    elif you == 'C':
        round_score += 3
    # calculate match:
    if opponent == you:
        round_score += 3
    elif opponent == 'A' and you == 'B':
        round_score += 6
    elif opponent == 'A' and you == 'C':
        round_score += 0
    elif opponent == 'B' and you == 'A':
        round_score += 0
    elif opponent == 'B' and you == 'C':
        round_score += 6
    elif opponent == 'C' and you == 'A':
        round_score += 6
    elif opponent == 'C' and you == 'B':
        round_score += 0
    print(f"{opponent=}, {you=} ==> {round_score = }")
    return round_score


with open("input.txt") as reader:
    rounds = reader.readlines()

# update list with substituting X,Y,Z with A,B,C for simplicity:
rounds_v2 = list(map(lambda x: x.replace('X', 'A').replace('Y', 'B').replace('Z', 'C'), rounds))

total_score = 0
for i, round in enumerate(rounds_v2):
    print(i, round.strip())
    print(f'round-{i} score: ', score:= get_score(round.split()[0], round.split()[1]))
    total_score += score

print(f"{total_score = }")


