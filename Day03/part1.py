import math, re

# messy :P
lengths = [[int(x), int(y), int(z)] for x, y, z in re.findall(r'(\d+)\s*(\d+)\s*(\d+).*\n', open('input.txt', 'r').read())]

errors = 0

for x, y, z in lengths:
    if (x + y <= z) or (y + z <= x) or (z + x <= y):
        errors += 1

print(len(lengths) - errors, 'valid triangles')
