#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    len_entradasys = len(sys.argv)
    if len_entradasys == 1:
        print("0 arguments.")
    elif len_entradasys == 2:
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(len_entradasys - 1))
        for i in range(1, len_entradasys):
            print("{:d}: {}".format(i, sys.argv[i]))
