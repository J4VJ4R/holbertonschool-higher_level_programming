#!/usr/bin/python3
def best_score(a_dictionary):
    s_max = max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
    return s_max
