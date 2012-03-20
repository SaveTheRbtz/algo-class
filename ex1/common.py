# -*- coding: utf-8 -*-

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

def debug(func):
    if not __debug__:
        return func
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        print "== {0} INPUT ==: ARGS: {1}, KWARGS: {2}".format(func.__name__, args, kwargs)
        ret = func(*args, **kwargs)
        print "== {0} OUTPUT ==: {1}".format(func.__name__, ret)
        return ret
    return wrapper
