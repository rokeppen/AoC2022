from aocd import lines, submit
from itertools import product, takewhile


def scores(matrix: list):
    result, n = [[0] * len(matrix[0]) for _ in range(len(matrix))], len(matrix) - 1
    for r in range(n, -1, -1):
        for c in range(len(matrix[0])):
            left = list(takewhile(lambda x: matrix[r][x] < matrix[r][c], range(c - 1, -1, -1)))
            down = list(takewhile(lambda x: matrix[x][c] < matrix[r][c], range(r + 1, n + 1)))
            result[r][c] = (len(left) + (1 if c and (not left or left[-1]) else 0)) * \
                           (len(down) + (1 if r < n and (not down or down[-1] < n) else 0))
    return result


if __name__ == '__main__':
    m = [list(map(int, line)) for line in lines]
    ld, ur = scores(m), list(zip(*scores(list(zip(*m)))))
    submit(max(ld[r][c] * ur[r][c] for r, c in product(range(len(m)), range(len(m[0])))), 'b')
