from aocd import lines, submit


if __name__ == '__main__':
    submit(sum(ord(line[2]) - 87 + ((ord(line[2]) - ord(line[0]) - 1) % 3) * 3 for line in lines), "a")
    submit(sum((ord(line[0]) + ord(line[2]) - 1) % 3 + 1 + (ord(line[2]) - 88) * 3 for line in lines), "b")
