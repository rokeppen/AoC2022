from aocd import data, submit


if __name__ == '__main__':
    calories = sorted(sum(map(int, elf.split('\n'))) for elf in data.split('\n\n'))
    submit(calories[-1], "a")
    submit(sum(calories[-3:]), "b")
