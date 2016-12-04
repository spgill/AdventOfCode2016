import re

raw = open('input.txt', 'r').read()
rooms = re.findall(r'(.*?)(\d{2,4})\[(.*?)\]\n', raw)

abet_str = 'abcdefghijklmnopqrstuvwxyz'
abet = [c for c in abet_str]

def checksum(s):
    data = {c: 0 for c in abet}
    for c in s:
        if c in abet:
            data[c] = data[c] + 1
    data = sorted(data.items(), key=lambda t: t[1], reverse=True)
    # print('DATA', data)
    groups = []
    i = 0
    while i < len(data):
        if data[i][1] == 0:
            break
        elif data[i + 1][1] == data[i][1]:
            seed = data[i]
            stub = [seed[0]]
            while i < len(data):
                if data[i + 1][1] == seed[1]:
                    stub.append(data[i + 1][0])
                    i += 1
                else:
                    i += 1
                    break
            groups.append(sorted(stub))
        else:
            groups.append([data[i][0]])
            i += 1
    # print('GROUPS', groups)

    check = ''
    for group in groups:
        for member in group:
            check += member
            if len(check) == 5:
                break
        if len(check) == 5:
            break
    return check

valid_rooms = []
for name, sector, check in rooms:
    if check == checksum(name):
        valid_rooms.append((name, int(sector), check))

def loop(n):
    '''Constrain a number N such that 0 <= i <= 25 in a loop'''
    while n > 25:
        n -= 26
    return n

for name, sector, check in valid_rooms:
    rotated = ''
    for char in name:
        if char == '-':
            rotated += ' '
            continue
        i = abet_str.index(char)
        i = loop(i + sector)
        rotated += abet_str[i]
    if rotated.startswith('northpole object storage'):
        print('Correct room sector ID is', sector)
        exit()
