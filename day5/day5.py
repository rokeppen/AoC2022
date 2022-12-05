from aocd import data, submit
from re import findall
from copy import deepcopy


def stack(proc, mover, part):
    for amount, fr, to in (map(int, findall(r'\d+', p)) for p in proc):
        mover[to - 1].extend(mover[fr - 1][-amount:][::-1 if part == "a" else 1])
        del mover[fr - 1][-amount:]
    submit("".join(s[-1] for s in mover), part)


if __name__ == '__main__':
    cm, procedures = map(lambda x: x.split("\n"), data.split("\n\n"))
    cm = [[cm[j][i] for j in range(len(cm) - 1) if cm[j][i].strip()][::-1] for i in range(1, len(cm[0]), 4)]
    stack(procedures, deepcopy(cm), "a")
    stack(procedures, deepcopy(cm), "b")
