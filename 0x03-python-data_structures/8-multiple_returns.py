#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        val = 0
        return sentence[val], None
    else:
        return len(sentence), sentence[0]
