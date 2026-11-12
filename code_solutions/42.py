import os

path = os.path.exapanduder("Desktop/project_euler/assets/words(42.py).text")

with open(path, "r") as f:
    content = f.read()

words = content.replace('"', '').split(',')

print(len(s))
print(words[:5])
