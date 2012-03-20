#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common import setup_signals, parse_file

PROGRESS_BAR = {}

def brute_force(data):
    """
    This function should return number of inversions of input stream

    >>> brute_force([1,2,3,4,5,6])
    0
    >>> brute_force([1,3,5,2,4,6])
    3
    >>> brute_force([6,5,4,3,2,1])
    15
    """
    global PROGRESS_BAR
    data = list(data)
    cnt = 0
    for i,a in enumerate(data):
        for j,b in enumerate(data):
            if i<j and a>b: cnt+=1
        PROGRESS_BAR.update({"PROGRESS": i, "FOUND": cnt})
    return cnt

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-f", type="string", dest="file", default="IntegerArray.txt")
    (options, args) = parser.parse_args()

    setup_signals(PROGRESS_BAR)

    print brute_force(parse_file(options.file))
