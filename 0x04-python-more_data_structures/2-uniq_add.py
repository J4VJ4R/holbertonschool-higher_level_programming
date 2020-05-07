#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    while my_list[suma] > 0:
        suma = suma + my_list[suma]
        suma = suma - 1
    return (suma)
