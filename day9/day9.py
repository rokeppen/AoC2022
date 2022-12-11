from numpy import sign
from aocd import lines, submit


class Position:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def move(self, direction: str):
        if direction in "UD":
            self.x += 1 if direction == "D" else -1
        else:
            self.y += 1 if direction == "R" else -1

    def shift(self, h):
        if abs(h.x - self.x) > 1:
            self.x, self.y = h.x + sign(self.x - h.x), h.y
        elif abs(h.y - self.y) > 1:
            self.x, self.y = h.x, h.y + sign(self.y - h.y)

    def copy(self):
        return Position(self.x, self.y)

    def __repr__(self):
        return str((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x.__hash__() + 31 * self.y.__hash__()


def walk(num_knots: int = 2):
    positions, knots = {Position()}, [Position() for _ in range(num_knots)]
    for d in "".join(motion[0] * int(motion[2:]) for motion in lines):
        knots[0].move(d)
        for i in range(num_knots - 1):
            knots[i + 1].shift(knots[i])
        positions.add(knots[-1].copy())
    return len(positions)


if __name__ == '__main__':
    submit(walk(), 'a')
    submit(walk(10), 'b')
