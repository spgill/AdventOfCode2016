import hashlib

door = open('input.txt', 'r').read().strip()

i = 0
passw = ''
while True:
    h = hashlib.md5((door + str(i)).encode()).hexdigest()
    if h[:5] == '00000':
        passw += h[5]
    i += 1
    if len(passw) == 8:
        break

print('Password:', passw)
