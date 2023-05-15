#!/usr/bin/python3
def multiple_returns(sentence):
    lenth_sent = len(sentence)
    if (lenth_sent == 0):
        new_tuple = (lenth_sent, None)
    else:
        new_tuple = (lenth_sent, sentence[0])
    return (new_tuple)
