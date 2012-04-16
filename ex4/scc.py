#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging as log
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from itertools import islice
from sys import maxint
from copy import deepcopy
from pprint import pformat

if __debug__:
    log.basicConfig(level=log.DEBUG)
else:
    log.basicConfig()

def main(G):
    log.warning("Number of Edges: %(total)d", dict(total=G.number_of_edges()))
    log.warning("Number of Nodes: %(total)d", dict(total=G.number_of_nodes()))
    return list(islice(sorted((len(lst) for lst in nx.algorithms.strongly_connected_components(G)), reverse=True), 5))

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-f", type="string", dest="file", default="SCC.txt.bz2")
    (options, args) = parser.parse_args()

    try:
        G = nx.read_adjlist(options.file, create_using=nx.DiGraph(), nodetype=int)
    except Exception:
        log.error("Can't parse file: %(file)s", dict(file=options.file), exc_info=True)
        exit(1)

    log.warning(main(G))
