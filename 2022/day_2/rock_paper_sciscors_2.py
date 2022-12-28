
def get_score(opponent, result):
    """calculate score for each round"""
    round_score = 0
    # get score based on your result:
    if result == 'X':  # Loose
        round_score += 0
        if opponent == 'A':
            round_score += 3
        elif opponent == 'B':
            round_score += 1
        elif opponent == 'C':
            round_score += 2

    elif result == 'Y':  # Draw
        round_score += 3
        if opponent == 'A':
            round_score += 1
        elif opponent == 'B':
            round_score += 2
        elif opponent == 'C':
            round_score += 3

    elif result == 'Z':  # Win!
        round_score += 6
        if opponent == 'A':
            round_score += 2
        elif opponent == 'B':
            round_score += 3
        elif opponent == 'C':
            round_score += 1

    print(f"{opponent=}, {result=} ==> {round_score = }")
    return round_score


with open("input.txt") as reader:
    rounds = reader.readlines()

total_score = 0
for i, round in enumerate(rounds):
    print('===')
    print(i, round.strip())
    print(f'round-{i} score: ', score:= get_score(round.split()[0], round.split()[1]))
    total_score += score

print(f"{total_score = }")


