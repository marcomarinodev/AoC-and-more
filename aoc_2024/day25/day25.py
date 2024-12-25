items = [{i for i, c in enumerate(item) if c == '#'}
    for item in open('input.txt').read().split('\n\n')]

print(sum(not k&l for k in items for l in items)//2)