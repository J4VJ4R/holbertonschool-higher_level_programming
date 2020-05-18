#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    lap = 0
    for i range(x):
        try:
            print("{}".format(my_list[i]), end="")
            lap += 1
        except IndexError:
            break
        print("")
        return (lap)
