from aocd import data, submit
from re import split, findall
from operator import mul
from functools import reduce


class Monkey:
    def __init__(self, config):
        self.business = 0
        self.items = list(map(int, split('items:|Operation', config)[1].strip().split(', ')))
        self.inspect = lambda old: eval(split('=|Test', config)[1].strip())
        self.divisible, self.true, self.false = map(int, findall(r'\d+', split('by', config)[1]))

    def turn(self, monkey_list: list, worry_decrease, top):
        for item in self.items:
            new = self.inspect(item) % top
            if worry_decrease:
                new //= 3
            monkey_list[self.false if new % self.divisible else self.true].items.append(new)
            self.business += 1
        self.items.clear()


def play_rounds(rounds: int, worry_decrease=False):
    monkeys = list(map(lambda x: Monkey(x), data.split("\n\n")))
    top = reduce(mul, (m.divisible for m in monkeys))
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.turn(monkeys, worry_decrease, top)
    return reduce(mul, sorted(map(lambda x: x.business, monkeys))[-2:])


if __name__ == '__main__':
    submit(play_rounds(20, True), 'a')
    submit(play_rounds(10000), 'b')
