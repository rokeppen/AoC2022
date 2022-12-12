from aocd import lines, submit


class Node:
    def __init__(self, name, size: int = 0, parent=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
        self.depth = parent.depth + 1 if parent else 0

    def magnitude(self):
        return self.size + sum(c.magnitude() for c in self.children)

    def walk(self, f, result):
        f(self, result)
        for c in self.children:
            c.walk(f, result)


class Tree:
    def __init__(self):
        self.root = Node('/', 0)
        self.current = self.root

    def cd(self, name: str):
        if name == "/":
            self.current = self.root
        elif name == "..":
            self.current = self.current.parent
        else:
            if name not in [c.name for c in self.current.children]:
                self.current.children.append(Node(name, parent=self.current))
            self.current = next(c for c in self.current.children if c.name == name)

    def add(self, size, name):
        self.current.children.append(Node(name, int(size), self.current))

    def walk(self, f, result: list):
        self.root.walk(f, result)
        return result


def search_smaller(node: Node, smaller: list):
    if node.magnitude() <= 100000 and not node.size:
        smaller.append(node.magnitude())


def search_big_enough(node: Node, big_enough: list):
    if 40000000 >= filetree.root.magnitude() - node.magnitude() and not node.size:
        big_enough.append(node.magnitude())


if __name__ == '__main__':
    filetree = Tree()
    for line in lines:
        if line.startswith("$ cd"):
            filetree.cd(line.split()[2])
        elif not (line.startswith("$") or line.startswith("dir")):
            filetree.add(*line.split())
    submit(sum(filetree.walk(search_smaller, [])), 'a')
    submit(min(filetree.walk(search_big_enough, [])), 'b')
