#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    sum = 0
    enter_arguments = len(sys.argv)
    if enter_arguments > 1:
        for i in sys.argv[1:]:
            sum = sum + int(i)
    print(sum)
