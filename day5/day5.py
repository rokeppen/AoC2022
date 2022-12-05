from aocd import data, submit
from re import findall
from copy import deepcopy


if __name__ == '__main__':
    cm9000, procedures = data.split("\n\n")
    cm9000, names = cm9000.rsplit("\n", 1)
    cm9000 = cm9000.split("\n")
    cm9000 = [[cm9000[j][i] for j in range(len(cm9000)) if cm9000[j][i].strip()][::-1] for i in range(1, len(names), 4)]
    cm9001 = deepcopy(cm9000)
    for amount, fr, to in [list(map(int, findall(r'\d+', procedure))) for procedure in procedures.split("\n")]:
        for _ in range(amount):
            cm9000[to - 1].append(cm9000[fr - 1].pop())
        cm9001[to - 1].extend(cm9001[fr - 1][-amount:])
        del cm9001[fr - 1][-amount:]
    submit("".join(stack[-1] for stack in cm9000), "a")
    submit("".join(stack[-1] for stack in cm9001), "b")
