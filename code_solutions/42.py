import os

path = os.path.expanduser("~/Desktop/project_euler/assets/words(42.py).txt")

with open(path, "r") as f:
    content = f.read()

words = content.replace('"', '').split(',')

def word_value(word):
    return sum(ord(x) - 64 for x in word)
def triangle_number(n):
    root = int((8 * n + 1)**0.5)
    return root * root = (8 * n + 1)
count_triangle_words = 0

for word in words:
    if triangle_number(word_value(word)):
        count_triangle_words += 1
print(count_triangle_words)
    

