#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    entradasys = sys.argv
    len_entradasys = len(entradasys)
    if len_entradasys == 1:
        print("0 arguments.")
        exit()
    elif len_entradasys == 2:
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(len_entradasys - 1))
        for i in range(1, len_entradasys):
            print("{:d}: {}".format(i, sys.argv[i]))