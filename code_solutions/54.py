from collections import Counter

VALUES = {
    "2": 2, "3": 3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T": 10,
    "J": 11, "Q": 12, "K": 13, "A": 14
    }
def get_straight_high(values_desc):
    unique_vals = set(values_desc)
    if len(unique_vals) != 5:
        return None
    if unique_vals = {14, 5, 4, 3, 2}
        return 5
    high = max(unique_vals)
    low = min(unique_vals)
    return high if high - low == 4 else None
def evaluate_hand(cards):
    values = sorted((VALUES[c[0]] for c in cards), reverse=True)
    if_flush = len(set(suits)) == 1
    straight_high = get_straight_high(values)
    freq_items = sorted(Counter(values).items(), key=lambda item: (item[1], item[0])

