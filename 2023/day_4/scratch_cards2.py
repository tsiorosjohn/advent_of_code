import json


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        lines_f = reader.readlines()
        for item in lines_f:
            input_ls.append(item.rstrip())
    return input_ls


def get_score(card_text):
    """
    get card text and find out how many winning numbers exist in each card.
    Then calculate points
    example:
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    """
    card_nr_f = card_text.split('|')[0].split(":")[0].split()[1]
    winning_nrs = card_text.split('|')[0].split(":")[1].split()
    own_nrs = card_text.split('|')[1].split()
    winning_nrs_int = [int(item) for item in winning_nrs]
    own_nrs_int = [int(item) for item in own_nrs]
    print(f"{winning_nrs = } // { winning_nrs_int = }")
    print(f"{own_nrs = } // {own_nrs_int = }")

    # find how many own numbers are winning ones:
    score_f = 0
    matches_f = 0
    for own_nr in own_nrs_int:
        if own_nr in winning_nrs_int:
            if matches_f == 0:
                score_f = 1
                matches_f += 1
            else:
                score_f *= 2
                matches_f += 1
            print(f"Card-{card_nr_f}: Own number {own_nr} wins! // {score_f = } - {matches_f = }")
    print(f"    >>> Card-{card_nr_f}: {score_f = } - {matches_f = }")

    return score_f, matches_f, card_nr_f


if __name__ == "__main__":
    # file = 'input.txt'
    file = 'example.txt'
    lines = parse_input(file)
    # print(lines)
    cards_d = {}
    summary = 0
    for line in lines:
        card_count = 1
        print('\n==========================')
        score, matches, card_nr = get_score(line)
        # if matches > 0:

        # sum += score
        cards_d[card_nr] = {'score': score, 'matches': matches, 'card_count': card_count}
    print(f"{cards_d}")

    for card, value in list(cards_d.items()):
        if cards_d[card]['matches'] > 0:
            print('card:', card, ', matches:', cards_d[card]['matches'])
            # first loop: increment 'card_count' per card and insert additional elements to dict:
            for i in range(int(card), int(card) + cards_d[card]['matches']):
                cards_d[str(i)]['card_count'] += 1
                cards_d[card+"_"+str(i)] = value

            # second loop: increment 'card_count' once more based on extra copy-cards obtained!:
            # for i in range(cards_d[str(card)]['card_count'] + 1):
            #     print(f"{i = }")
            #     cards_d[card]['card_count'] += 1

    print(f"updated {json.dumps(cards_d, indent=4)}")
