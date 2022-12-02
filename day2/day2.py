if __name__ == '__main__':
    print(sum(ord(line[2]) - 87 + ((ord(line[2]) - ord(line[0]) - 1) % 3) * 3 for line in open('input.txt')))
    print(sum((ord(line[0]) + ord(line[2]) - 1) % 3 + 1 + (ord(line[2]) - 88) * 3 for line in open('input.txt')))
