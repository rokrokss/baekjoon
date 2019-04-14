import sys


class Tree():
    def __init__(self, age, next_tree=None):
        self.age = age
        self.next_tree  = next_tree

    def set_next(self, new_next):
        self.next_tree = new_next


class TreePriorityQueue():
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, tree):
        self.length += 1
        current = self.head
        if current is None:
            self.head = tree
            return
        while current:
            if current.next_tree is None:
                current.set_next(tree)
                return
            if current.age <= tree.age and tree.age <= current.next_tree.age:
                tree.next_tree = current.next_tree
                current.next_tree = tree
                return
            current = current.next_tree

    def insert_front(self, tree):
        self.length += 1
        tree.next_tree = self.head
        self.head = tree


read = sys.stdin.readline
n, m, k = map(int, read().split())
grid = [[5 for _ in range(n)] for _ in range(n)]
power = [list(map(int, read().split())) for _ in range(n)]
trees = [[TreePriorityQueue() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, read().split())
    trees[x-1][y-1].insert(Tree(z))
for _ in range(k):
    # 봄, 여름
    for i in range(n):
        for j in range(n):
            if not (trees[i][j].head is None):
                current = trees[i][j].head
                previous = None
                power_stock = 0
                while not (current is None):
                    if current.age <= grid[i][j]:
                        grid[i][j] -= current.age
                        current.age += 1
                        previous = current
                    else:
                        power_stock += current.age // 2
                        if previous is None:
                            trees[i][j].head = current.next_tree
                        else:
                            previous.set_next(current.next_tree)
                        trees[i][j].length -= 1
                    current = current.next_tree
                grid[i][j] += power_stock
    # 가을
    for i in range(n):
        for j in range(n):
            if not (trees[i][j].head is None):
                current = trees[i][j].head
                while not (current is None):
                    if current.age % 5 == 0:
                        if i > 0:
                            trees[i-1][j].insert_front(Tree(1))
                            if j > 0:
                                trees[i-1][j-1].insert_front(Tree(1))
                            if j < n-1:
                                trees[i-1][j+1].insert_front(Tree(1))
                        if i < n-1:
                            trees[i+1][j].insert_front(Tree(1))
                            if j > 0:
                                trees[i+1][j-1].insert_front(Tree(1))
                            if j < n-1:
                                trees[i+1][j+1].insert_front(Tree(1))
                        if j > 0:
                            trees[i][j-1].insert_front(Tree(1))
                        if j < n-1:
                            trees[i][j+1].insert_front(Tree(1))
                    current = current.next_tree
    # 겨울
    for i in range(n):
        for j in range(n):
            grid[i][j] += power[i][j]
ans = 0
for i in range(n):
    for j in range(n):
        ans += trees[i][j].length
print(ans)

