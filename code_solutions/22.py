with open('names_scores_pe.txt', 'r') as f:
    content = f.read()
    names = sorted([name.replace('"', '') for name in content.split(',')])
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
total_name_scores = 0
for position, name in enumerate(names, start=1):
    letter_sum = 0
    for char in name:
        value = alphabet.index(char) + 1
        letter_sum += value
    name_score = letter_sum * position
    total_name_scores += name_score
print(total_name_scores)


