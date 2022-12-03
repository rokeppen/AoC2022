def priorities(chars):
    print(sum(map(lambda c: ord(c.lower()) - 96 + 26 * c.isupper(), chars)))


if __name__ == '__main__':
    priorities((set(line[:len(line) // 2]) & set(line[len(line) // 2:])).pop() for line in open('input.txt'))
    priorities(set.intersection(*map(lambda x: set(x.strip()), t)).pop() for t in zip(*[open('input.txt')] * 3))

