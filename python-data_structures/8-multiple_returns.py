#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[:1] if len(sentence) > 0 else None
    newtuple = (len(sentence), first)
    return newtuple
