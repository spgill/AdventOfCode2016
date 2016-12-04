import math, sys

instructions = open('input.txt', 'r').read().strip().split('\n')

clamp = lambda lower, x, upper: max(lower, min(x, upper))

lookup = [
    [None, None, 'D', None, None],
    [None, 'A', 'B', 'C', None],
    ['5', '6', '7', '8', '9'],
    [None, '2', '3', '4', None],
    [None, None, '1', None, None],
]
angles = {'U': 0.5, 'R': 0.0, 'D': -0.5, 'L': -1.0}

posx = 0
posy = 2

for line in instructions:
    for direction in line:
        newx = clamp(0, posx + int(math.cos(math.pi * angles[direction])), 4)
        if lookup[posy][newx]:
            posx = newx

        newy = clamp(0, posy + int(math.sin(math.pi * angles[direction])), 4)
        if lookup[newy][posx]:
            posy = newy

    sys.stdout.write(lookup[posy][posx])
    # print(posx, posy, lookup[posy][posx])
print()
