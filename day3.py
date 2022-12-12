from aocd import lines, submit


def prio(chars):
    return sum(ord(c.lower()) - 96 + 26 * c.isupper() for c in chars)


if __name__ == '__main__':
    submit(prio((set(l[:len(l) // 2]) & set(l[len(l) // 2:])).pop() for l in lines), 'a')
    submit(prio(set.intersection(*map(set, lines[i:i + 3])).pop() for i in range(0, len(lines), 3)), 'b')
