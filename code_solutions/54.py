from collections import Counter

values = {r: i for i, r in enumerate('23456789TJQKA', start=2)}
straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 4, -1)]
ranks = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (), (), (3, 2), (4, 1)]

def hand_rank(hand):
    counts = Counter(card[0] for card in hand)
    sorted_counts = sorted(((v, values[k]) for k, v in counts.items()), reverse=True)
    score = list(zip(*sorted_counts))
    try:
        if score[1]==(14, 5, 4, 3, 2): score[1] = (5, 4, 3, 2, 1)
        score[0] = ranks.index(score[0])
    except ValueError:
        score[0] = 0
    if len(set(card[1] for card in hand)) == 1:
        score[0] = 5
    if score[1] in straights:
        score[0] = 8 if score[0] == 5 else 4
    return score

for _ in range(int(input())):
    hand = input().split()
    player1, player2 = hand[:5], hand[5:]
    print("Player 1" if hand_rank(player1) > hand_rank(player2) else "Player 2")
