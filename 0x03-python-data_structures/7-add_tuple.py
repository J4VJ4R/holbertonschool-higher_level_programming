#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in range(len(tuple_a)):
        for j in range(len(tuple_a[0])):
            result[i][j] = tuple_a[i][j] + tuple_b[i][j]
    for r in result:
        print(r)
