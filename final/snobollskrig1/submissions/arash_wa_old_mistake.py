#! /usr/bin/python3
"""
Arash WA
"""
import sys
import collections
import heapq
from pprint import pprint


def main():
    stdin_lines = []
    for line in sys.stdin:
        if line.strip() != "":
            stdin_lines.append(line.strip())

    # parse step 1
    n, l, _m = map(int, stdin_lines[0].split())
    # parse step 2
    start_positions = list(map(int, stdin_lines[1:l+1]))
    # parse step 3
    graph = collections.defaultdict(list)
    Edge = collections.namedtuple('Edge', 'dest weight')
    for line in stdin_lines[l+1:]:
        v1, v2, w = map(int, line.split())
        e1 = Edge(v2, w)
        e2 = Edge(v1, w)
        graph[v1].append(e1)
        graph[v2].append(e2)
    # Done parsing, start solving
    answer = solve(start_positions, graph)
    for (a, b) in answer:
        print(a, b)


def solve(start_positions, graph):
    answer = set()
    heap = [(0, node_ix, country_ix) for (country_ix, node_ix) in
            enumerate(start_positions)]
    heapq.heapify(heap)
    Owners = collections.namedtuple('Owners', 'time owners_set')
    owners_map = {}
    while heap:
        t0 = heap[0][0]
        vs = []
        cs = []
        while heap and heap[0][0] == t0:
            (_t0, v0, c0) = heapq.heappop(heap)
            vs.append(v0)
            cs.append(c0)
        for (v0, c0) in zip(vs, cs):
            if v0 in owners_map:
                for c in owners_map[v0].owners_set:
                    answer.add(frozenset((c0, c)))
                owners_map[v0].owners_set.add(c0)
            else:
                owners_map[v0] = Owners(t0, {c0})
        for (v0, c0) in zip(vs, cs):
            if owners_map[v0] == Owners(t0, {c0}):
                # I we just came, and we are the only ones who came
                # Otherwise, we're not allowed to continue from this node
                for edge in graph[v0]:
                    if edge.dest in owners_map:
                        # It's a conquered node, lets attack unconditionally
                        for c in owners_map[edge.dest].owners_set:
                            answer.add(frozenset((c0, c)))
                    else:
                        # It's free to try to reach
                        heapq.heappush(heap, (t0 + edge.weight, edge.dest, c0))
    return sorted((sorted(x) for x in answer if len(x) > 1))


if __name__ == '__main__':
    main()

