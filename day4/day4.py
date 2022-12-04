from aocd import lines, submit
from numpy import sign
from re import split


if __name__ == '__main__':
    pairs = [tuple(map(int, split(',|-', x))) for x in lines]
    submit(sum(sign((x1 - x2) * (y1 - y2)) <= 0 for x1, y1, x2, y2 in pairs), 'a')
    submit(sum(sign((y1 - x2) * (x1 - y2)) <= 0 for x1, y1, x2, y2 in pairs), 'b')
