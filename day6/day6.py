from aocd import data, submit


def window(w):
    return next(i + w for i in range(len(data)) if len(set(data[i:i + w])) == w)


if __name__ == '__main__':
    submit(window(4), "a")
    submit(window(14), "b")
