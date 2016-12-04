import math, re

# messy :P
col1 = []
col2 = []
col3 = []
[[col1.append(int(x)), col2.append(int(y)), col3.append(int(z))] for x, y, z in re.findall(r'(\d+)\s*(\d+)\s*(\d+).*\n', open('input.txt', 'r').read())]
lengths = col1 + col2 + col3

errors = 0
valid = 0

def by3(l):
    triple = []
    for entry in l:
        triple.append(entry)
        if len(triple) == 3:
            yield triple
            triple = []

for x, y, z in by3(lengths):
    if (x + y <= z) or (y + z <= x) or (z + x <= y):
        errors += 1
    else:
        valid += 1

print(valid, 'valid triangles')
