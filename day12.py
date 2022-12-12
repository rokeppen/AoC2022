from aocd import lines, submit
from numpy import inf
from itertools import product
from collections import defaultdict


def is_neighbour(graph, fr, to):
    return ord(graph[fr[0]][fr[1]]) - 2 < ord(graph[to[0]][to[1]]) \
        and ((abs(fr[0] - to[0]) < 2 and fr[1] == to[1]) or (abs(fr[1] - to[1]) < 2 and fr[0] == to[0]))


def find(graph, char, by):
    n = len(lines[0])
    results = [(i // n, i % n) for i in range(len("".join(lines))) if graph[i // n][i % n] == char]
    for result in results:
        graph[result[0]][result[1]] = by
    return results


def dijkstra(graph, src):
    queue, prev, dist = list(product(range(len(graph)), range(len(graph[0])))), dict(), defaultdict(lambda: inf)
    dist[src] = 0
    while len(queue):
        u = sorted(queue, key=lambda x: dist[x])[0]
        queue.remove(u)
        for n in (v for v in queue if is_neighbour(graph, u, v)):
            alt = dist[u] + 1
            if alt < dist[n]:
                dist[n] = alt
                prev[n] = u
    return dist


if __name__ == '__main__':
    m = [list(line) for line in lines]
    source = find(m, 'S', 'a')[0]
    distances = dijkstra(m, find(m, 'E', 'z')[0])
    submit(distances[source], 'a')
    submit(min(distances[d] for d in find(m, 'a', 'a')), 'b')
