seq = range(10)
print(seq, type(seq))
print(list(seq[5:]))
print(len(seq[5:]))

for i in seq:
    print(i, end=' ')
else:
    print()

print('ok')

for i in range(-10, 0, 1):
    print(i, end=' ')
else:
    print()

for i in range(0, 10, 1):
    print(i, end=' ')
else:
    print()

