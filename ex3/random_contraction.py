#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging as log
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from itertools import izip_longest
from sys import maxint
from copy import deepcopy
from pprint import pformat
from random import choice, seed, randint

if __debug__:
    log.basicConfig(level=log.DEBUG)
else:
    log.basicConfig()

def random_contraction(G, random_seed=None):
    """
    Preforms random contraction algorithm on graph.
    ``random_seed`` is used for determenistic runs for example for doctests.
    Returns number of edges in mincut.

    >>> G = nx.MultiGraph()
    >>> G.add_edges_from([('1', '3'), ('1', '2'), ('1', '4'), ('3', '2'), ('3', '4'), ('2', '4')])
    >>> [random_contraction(deepcopy(G),i) for i in xrange(10)]
    [3, 4, 3, 4, 3, 3, 3, 3, 3, 3]

    XXX: Too much debug info
    """
    if random_seed is not None:
        seed(random_seed)

    log.info("Initial nodes: %(nodes)s", dict(nodes=G.nodes()))
    log.info("Initial edges: %(edges)s", dict(edges=G.edges()))
    while G.number_of_nodes() > 2:
        node1, node2 = choice(G.edges())
        log.debug("Choice is %(node1)s <-> %(node2)s ", dict(node1=node1, node2=node2))
        if node1 == node2:
            log.debug("Cirrcular link found on node: %(node1)s", dict(node1=node1))
            continue
        log.debug("Node's %(node1)s neighbors: %(neighbors)s", dict(node1=node1, neighbors=G.neighbors(node1)))
        for neighbor in G.neighbors(node1):
            while neighbor in set(G.neighbors(node1)) - set([node2]):
                G.add_edge(neighbor, node2)
                G.remove_edge(neighbor, node1)
                log.debug("New edge: %(neighbor)s <-> %(node2)s", dict(neighbor=neighbor, node2=node2))
        log.debug("Removing node: %(node1)s", dict(node1=node1))
        G.remove_node(node1)
        log.debug("Nodes: %(nodes)s", dict(nodes=G.nodes()))
        log.debug("Edges: %(edges)s", dict(edges=G.edges()))

    log.info("Number of edges: %(edges)s", dict(edges=G.number_of_edges()))
    return G.number_of_edges()

def main(raw_pairs, iterations, random_seed):
    G = nx.MultiGraph()
    G.add_edges_from(raw_pairs)

    log.warning("Edges: %(edges)s", dict(edges=G.edges()))
    log.warning("Number of Edges: %(total)d", dict(total=G.number_of_edges()))
    log.warning("Nodes: %(nodes)s", dict(nodes=G.nodes()))
    log.warning("Number of Nodes: %(total)d", dict(total=G.number_of_nodes()))

    if __debug__:
        nx.draw(G)
        plt.show()

    if random_seed is None:
        random_seed = randint(0, maxint)

    return min(random_contraction(deepcopy(G), random_seed + i) for i in xrange(iterations))

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-f", type="string", dest="file", default="kargerAdj.txt")
    parser.add_option("-i", type="int", dest="iterations", default=100)
    parser.add_option("-s", type="int", dest="random_seed")
    (options, args) = parser.parse_args()

    raw_pairs = []
    with open(options.file) as lines:
        for line in lines:
            try:
                node, connections = np.split(line.split(), [1])
                node, = node
                for x,y in izip_longest([node], connections, fillvalue=node):
                    if (y, x) in raw_pairs or (x, y) in raw_pairs:
                        continue
                    raw_pairs.append((x, y))
            except Exception:
                log.info("Can't parse line: %(line)s", dict(line=line), exc_info=True)

    log.debug("Raw Pairs: %(raw_pairs)s", dict(raw_pairs=pformat(raw_pairs)))
    log.warning("Mincut is: %(mincut)s", dict(mincut=main(raw_pairs, options.iterations, options.random_seed)))
