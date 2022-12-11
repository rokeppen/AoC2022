from aocd import lines, submit


def visible(from_row, row, reverse=1):
    curr_max, result = -1, set()
    for i, value in enumerate(map(int, list(row[::reverse]))):
        if value > curr_max:
            result.add((from_row, i if reverse == 1 else len(row) - i - 1))
            curr_max = value
    return result


def traverse(data):
    return set.union(*(visible(i, line) | visible(i, line, -1) for i, line in enumerate(data)))


if __name__ == '__main__':
    submit(len(traverse(lines) | set(map(lambda x: x[::-1], traverse(zip(*lines))))), 'a')
