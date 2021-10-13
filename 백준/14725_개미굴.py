# 4
# 2 KIWI BANANA
# 2 KIWI APPLE
# 2 APPLE APPLE
# 3 APPLE BANANA KIWI
from collections import defaultdict


class Node:
    def __init__(self, value):
        self.key = value
        self.children = dict()


class Trie:

    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]

    def printStructure(self, L, curr_node):
        if L == 0:
            curr_node = self.head

        for child in sorted(curr_node.children.keys()):
            print("--" * L, child, sep="")
            self.printStructure(L + 1, curr_node.children[child])


n = int(input())
trie = Trie()
for _ in range(n):
    data = input().split()
    trie.insert(data[1:])

trie.printStructure(0, 0)
