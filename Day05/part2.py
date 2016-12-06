import hashlib

door = open('input.txt', 'r').read().strip()

i = 0
passw = [None for i in range(8)]
while True:
    h = hashlib.md5((door + str(i)).encode()).hexdigest()
    if h[:5] == '00000':
        try:
            j = int(h[5])
        except ValueError:
            i += 1
            continue
        if j < len(passw) and not passw[j]:
            passw[j] = h[6]
            print(door + str(i), h, passw)
    i += 1
    if None not in passw:
        break

print('Password:', ''.join(passw))
