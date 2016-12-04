import math

with open('input.txt', 'r') as input_file:
    directions = input_file.read().strip().split(', ')

angle = 90
posx = 0
posy = 0
history = set()
history.add((0, 0))
twice = None

for entry in directions:
    heading = entry[0]
    distance = int(entry[1:])
    if heading == 'L':
        angle += 90
    elif heading == 'R':
        angle -= 90
    else:
        raise RuntimeError('wtf')

    movex = int(math.cos(math.radians(angle)))
    movey = int(math.sin(math.radians(angle)))

    for i in range(distance):
        posx += movex
        posy += movey
        pos = (posx, posy)

        if pos in history and not twice:
            twice = pos
        else:
            history.add(pos)

print('Part one:', abs(posx) + abs(posy))
print('Part two:', abs(twice[0]) + abs(twice[1]))
