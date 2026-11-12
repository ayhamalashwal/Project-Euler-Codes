import os

path = os.path.expanduser("~/Desktop/project_euler/assets/words(42.py).txt")

with open(path, "r") as f:
    content = f.read()

words = content.replace('"', '').split(',')

print(len(words))
print(words[:5])
