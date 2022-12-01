if __name__ == '__main__':
    with open('input.txt') as file:
        calories = [sum(map(int, elf.split('\n'))) for elf in file.read().rstrip().split('\n\n')]
        print(max(calories))
        print(sum(sorted(calories)[-3:]))

