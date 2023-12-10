import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def get_score(card_text):
    """
    get card text and find out how many winning numbers exist in each card.
    Then calculate points
    example:
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    """
    card_nr = card_text.split('|')[0].split(":")[0].split()[1]
    winning_nrs = card_text.split('|')[0].split(":")[1].split()
    own_nrs = card_text.split('|')[1].split()
    winning_nrs_int = [int(item) for item in winning_nrs]
    own_nrs_int = [int(item) for item in own_nrs]
    print(f"{winning_nrs = } // { winning_nrs_int = }")
    print(f"{own_nrs = } // {own_nrs_int = }")

    # find how many own numbers are winning ones:
    score = 0
    matches = 0
    for own_nr in own_nrs_int:
        if own_nr in winning_nrs_int:
            if matches == 0:
                score = 1
                matches += 1
            else:
                score *= 2
                matches += 1
            print(f"Card-{card_nr}: Own number {own_nr} wins! // {score = } - {matches = }")
    print(f"    >>> Card-{card_nr}: {score = } - {matches = }")

    return score


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    # print(lines)
    sum = 0
    for line in lines:
        print('\n==========================')
        score = get_score(line)
        sum += score

    print(f"Total score:{sum}")
