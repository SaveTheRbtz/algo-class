#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common import parse_file
import itertools

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
    return sum(1 for a,b in itertools.combinations(data, 2) if a > b)

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-f", type="string", dest="file", default="IntegerArray.txt")
    (options, args) = parser.parse_args()

    print brute_force(parse_file(options.file))
