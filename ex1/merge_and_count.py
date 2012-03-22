#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common import parse_file, debug

@debug
def merge_and_count(left, right):
    """
    Merge two sorted lists and return number of inversions
    Not very optimized but pretty pythonish

    >>> merge_and_count([6], [5])
    (1, [5, 6])
    >>> merge_and_count([1, 2, 3], [4, 5, 6])
    (0, [1, 2, 3, 4, 5, 6])
    >>> merge_and_count([1, 3, 5], [2, 4, 6])
    (3, [1, 2, 3, 4, 5, 6])
    >>> merge_and_count([1, 2, 3], [4, 5, 6, 7])
    (0, [1, 2, 3, 4, 5, 6, 7])
    >>> merge_and_count([1, 2], [4, 5, 6])
    (0, [1, 2, 4, 5, 6])
    """
    split_inversions = 0
    sorted_list = []
    while left and right:
        if left < right:
            sorted_list.append(left.pop(0))
        else:
            split_inversions += len(left)
            sorted_list.append(right.pop(0))
    return split_inversions, sorted_list + left + right

@debug
def sort_and_count(lst):
    """
    This function should return number of inversions of input list

    >>> sort_and_count([1, 2, 3, 4, 5, 6])
    (0, [1, 2, 3, 4, 5, 6])
    >>> sort_and_count([1, 3, 5, 2, 4, 6])
    (3, [1, 2, 3, 4, 5, 6])
    >>> sort_and_count([6, 5, 4, 3, 2, 1])
    (15, [1, 2, 3, 4, 5, 6])
    """
    left, right = lst[:len(lst) / 2], lst[len(lst) / 2:]
    # Trivial case
    if len(lst) <= 2:
        if not right or left < right:
            return 0, lst
        else:
            return 1, right + left
    # Recursive case
    inv_left, sorted_left = sort_and_count(left)
    inv_right, sorted_right = sort_and_count(right)
    split_inversions, sorted_list = merge_and_count(sorted_left, sorted_right)
    return inv_left + inv_right + split_inversions, sorted_list

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-f", type="string", dest="file", default="IntegerArray.txt")
    (options, args) = parser.parse_args()

    inversions, _ = sort_and_count(list(parse_file(options.file)))
    print inversions
