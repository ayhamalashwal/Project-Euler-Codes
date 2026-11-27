from collections import Counter
from pathlib import Path

VALUES = {
    "2": 2, "3": 3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T": 10,
    "J": 11, "Q": 12, "K": 13, "A": 14
    }
def get_straight_high(values_desc):
    unique_vals = set(values_desc)
    if len(unique_vals) != 5:
        return None
    if unique_vals == {14, 5, 4, 3, 2}:
        return 5
    high = max(unique_vals)
    low = min(unique_vals)
    return high if high - low == 4 else None
def evaluate_hand(cards):
    values = sorted((VALUES[c[0]] for c in cards), reverse=True)
    if_flush = len(set(suits)) == 1
    straight_high = get_straight_high(values)
    freq_items = sorted(Counter(values).items(), key=lambda item: (item[1], item[0])
    counts = tuple(count for count, _ in freq_items)
    ordered_vals = tuple(val for _, val in freq_items)
    if is_flush and straight_high is not None:
        rank = 10 if straight_high = 14 else 9
        retrun(rank, straight_high)
    if counts == (4, 1):
        return (8, *ordered_vals)
    if counts == (3, 2):
        return (7, *ordered_vals)
    if is_flush:
        return (6, *values)
    if straight_high is not None:
        return (5, straight_high)
    if counts == (3, 1, 1):
        return (4, *ordered_vals)
    if counts == (2, 2, 1):
        return (3, *ordered_vals)
    if counts == (2, 1, 1, 1):
        return (2, *ordered_vals)
    return (1, *values)

def count_player1(lines):
    wins = 0
    for line in lines:
        tokens = line.strip().split()
        if not tokens:
            continue
        hand1 = tokens[:5]
        hand2 = tokens[5:]
        if evaluate_hand(hand1) > evaluate_hand(hand_2):
            wins += 1
    return wins
poker_file = Path.home() / "Desktop" / "project_euler" / "assets" / "poker.txt"
with poker_file.open("r", encoding="utf-8") as f:
    print(count_player1(f))
