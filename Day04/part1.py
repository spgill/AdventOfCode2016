import re

raw = open('input.txt', 'r').read()
rooms = re.findall(r'(.*?)(\d{2,4})\[(.*?)\]\n', raw)

abet = [c for c in 'abcdefghijklmnopqrstuvwxyz']

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

sum_sector = 0
for name, sector, check in rooms:
    if check == checksum(name):
        sum_sector += int(sector)

print('Sum of sectors', sum_sector)
