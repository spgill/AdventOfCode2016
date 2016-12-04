import math

instructions = open('input.txt', 'r').read().strip().split('\n')

clamp = lambda lower, x, upper: max(lower, min(x, upper))

lookup = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
angles = {'U': 0.5, 'R': 0.0, 'D': -0.5, 'L': -1.0}

posx = 1
posy = 1

for line in instructions:
    for direction in line:
        posx += int(math.cos(math.pi * angles[direction]))
        posx = clamp(0, posx, 2)

        posy += int(math.sin(math.pi * angles[direction]))
        posy = clamp(0, posy, 2)

    sys.stdout.write(lookup[posy][posx])
print()
