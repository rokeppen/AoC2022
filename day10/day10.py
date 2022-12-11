from aocd import lines, submit


if __name__ == '__main__':
    states, register, n = [], 1, 40
    for line in lines:
        states.append(register)
        if line != "noop":
            states.append(register)
            register += int(line.split()[1])
    submit(sum((20 + i * n) * v for i, v in enumerate(states[19::n])), "a")
    print("".join(("" if x % n or not x else "\n") + ('#' if abs(s - x % n) < 2 else '.') for x, s in enumerate(states)))
