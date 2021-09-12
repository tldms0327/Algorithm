import sys

# to avoid runtime error
sys.setrecursionlimit(1000000)


def solution(nodeinfo):
    nodeinfo = sorted([[i + 1] + nodeinfo[i] for i in range(len(nodeinfo))], key=lambda x: (x[2], -x[1]), reverse=True)
    root = nodeinfo[0]
    root_node = Node(root[0], root[1], root[2])
    now_y = root[2]
    floor = -1
    # nodeinfo를 토대로 트리 만들기
    for point in nodeinfo[1:]:
        if point[2] != now_y:
            now_y = point[2]
            floor += 1
        i = floor
        now_node = root_node
        # 루트부터 한 측(floor)씩 내려가면서 새로 추가되는 노드의 부모 노드(now_node) 찾기
        while i > 0:
            if point[1] < now_node.x:
                now_node = now_node.left
            else:
                now_node = now_node.right
            i -= 1
        # 리프 토드로 추가
        if point[1] < now_node.x:
            now_node.left = Node(point[0], point[1], point[2])
        else:
            now_node.right = Node(point[0], point[1], point[2])

    answer = [preorder_traversal(root_node), postorder_traversal(root_node)]

    return answer


def preorder_traversal(root):
    # Left ->Right -> Root
    answer = []
    if root is not None:
        answer.append(root.index)
        answer += preorder_traversal(root.left)
        answer += preorder_traversal(root.right)

    return answer


def postorder_traversal(root):
    # Left ->Right -> Root
    answer = []
    if root is not None:
        answer = postorder_traversal(root.left)
        answer += postorder_traversal(root.right)
        answer.append(root.index)

    return answer


class Node:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y
        self.left = None
        self.right = None


N = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2]]
print(solution(N))
