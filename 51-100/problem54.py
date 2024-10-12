from collections import Counter

TIEBREAKER_PADDING_MULTIPLIER = 100 ** 5

HIGH_CARD       = 0
ONE_PAIR        = 1 * TIEBREAKER_PADDING_MULTIPLIER
TWO_PAIR        = 2 * TIEBREAKER_PADDING_MULTIPLIER
THREE_OF_A_KIND = 3 * TIEBREAKER_PADDING_MULTIPLIER
STRIAGHT        = 4 * TIEBREAKER_PADDING_MULTIPLIER
FLUSH           = 5 * TIEBREAKER_PADDING_MULTIPLIER
FULL_HOUSE      = 6 * TIEBREAKER_PADDING_MULTIPLIER
FOUR_OF_A_KIND  = 7 * TIEBREAKER_PADDING_MULTIPLIER
STRIAGHT_FLUSH  = 8 * TIEBREAKER_PADDING_MULTIPLIER
ROYAL_FLUSH     = 9 * TIEBREAKER_PADDING_MULTIPLIER

def get_tiebreak_value(card_values):
    value_counts = Counter(card_values)
    card_values.sort(key=lambda v: value_counts[v] * 100 + v, reverse=True)
    tb = 0
    for i in range(len(card_values)):
        tb += card_values[i] * (100 ** (4-i))
    return tb

def get_card_rank(c):
    if c == "T":
        return 10
    elif c == "J":
        return 11
    elif c == "Q":
        return 12
    elif c == "K":
        return 13
    elif c == "A":
        return 14
    else:
        return int(c)

def parse_hand(hand):
    return [(get_card_rank(c[0]), c[1]) for c in hand]

def rank_hand(hand):
    suits = Counter([c[1] for c in hand])
    values = sorted([c[0] for c in hand])
    value_counter = Counter(values)

    are_all_cards_same_suit = len(suits) == 1
    are_all_cards_sequential = True
    for i in range(1, len(values)):
        if values[i] != values[i-1] + 1:
            are_all_cards_sequential = False
            break

    if are_all_cards_same_suit and are_all_cards_sequential and values[0] == 10:
        return ROYAL_FLUSH
    
    if are_all_cards_same_suit and are_all_cards_sequential:
        return STRIAGHT_FLUSH + get_tiebreak_value(values)
    
    if are_all_cards_same_suit:
        return FLUSH + get_tiebreak_value(values)
    
    if are_all_cards_sequential:
        return STRIAGHT + get_tiebreak_value(values)
    
    if 4 in value_counter.values():
        return FOUR_OF_A_KIND + get_tiebreak_value(values)
    
    if 3 in value_counter.values() and 2 in value_counter.values():
        return FULL_HOUSE + get_tiebreak_value(values)
    
    if 3 in value_counter.values():
        return THREE_OF_A_KIND + get_tiebreak_value(values)
    
    num_pairs = 0
    pair_values = []
    for k in value_counter.keys():
        if value_counter[k] == 2:
            num_pairs += 1
            pair_values.append(k)

    if num_pairs == 2:
        return TWO_PAIR + get_tiebreak_value(values)
    
    if num_pairs == 1:
        return ONE_PAIR + get_tiebreak_value(values)
    
    return get_tiebreak_value(values)

def does_hand1_win(hand1, hand2):
    hand1_rank = rank_hand(hand1)
    hand2_rank = rank_hand(hand2)
    return hand1_rank > hand2_rank

with open("51-100/input/0054.txt") as f:
    games = f.readlines()

player1_wins = 0
for game in games:
    hands = game.strip().split(" ")
    hand1 = parse_hand(hands[:5])
    hand2 = parse_hand(hands[5:])
    if does_hand1_win(hand1, hand2):
        player1_wins += 1

print(player1_wins)
