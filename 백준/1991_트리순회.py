# 전위순위: root - l - r
# 중위순위: l - root - r
# 후위순위: l - r - root

def inorder_traversal(tree, root):
    # Left -> Root -> Right
    answer = ''
    if root != '.':
        answer = inorder_traversal(tree, tree[root]['left'])
        answer += root
        answer += inorder_traversal(tree, tree[root]['right'])
    return answer


def postorder_traversal(tree, root):
    # Left ->Right -> Root
    answer = ''
    if root != '.':
        answer = postorder_traversal(tree, tree[root]['left'])
        answer += postorder_traversal(tree, tree[root]['right'])
        answer += root

    return answer


def preorder_traversal(tree, root):
    # Left ->Right -> Root
    answer = ''
    if root != '.':
        answer += root
        answer += preorder_traversal(tree, tree[root]['left'])
        answer += preorder_traversal(tree, tree[root]['right'])

    return answer


n = int(input())
TREE = dict()

for _ in range(n):
    root, left, right = input().split()
    TREE[root] = {'left': left, 'right': right}

print(preorder_traversal(TREE, 'A'))
print(inorder_traversal(TREE, 'A'))
print(postorder_traversal(TREE, 'A'))
