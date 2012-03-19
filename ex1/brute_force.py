#!/usr/bin/env python
# -*- coding: utf-8 -*-

PROGRESS_BAR = {}

def setup_signals(progress_bar):
    import signal
    def progress(*args):
        print progress_bar
    for sig in (signal.SIGINFO, signal.SIGQUIT):
        signal.signal(sig, progress)
    print "Signal handlers installed:"
    print "Press Ctrl+T(BSD) / Ctrl+4(Linux) for progress"

def parse_file(filename):
    """Load list of integers from file and yield them"""
    with open(filename) as f:
        for line in f:
            for num in map(int, line.split()):
                yield num

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
