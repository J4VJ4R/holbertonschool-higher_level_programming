#!/usr/bin/python3
for i in range(99):
    if i / 10 < i % 10 and i != 89:
        print('{:02d},'.format(i), end=' ')
print(89)
