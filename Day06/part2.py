words = open('input.txt', 'r').read().strip().split('\n')

abet = 'abcdefghijklmnopqrstuvwxyz'
columns = []

for i in range(8):
    columns.append({char: 0 for char in abet})

for word in words:
    for i, char in enumerate(word):
        columns[i][char] += 1

message = ''

for column in columns:
    message += sorted(column.items(), key=lambda t: t[1], reverse=False)[0][0]

print('Message:', message)
