with open('names_scores_pe.txt', 'r') as f:
    content = f.read()
    names = sorted([name.replace('"', '') for name in content.split(',')])
print(names[:5])
