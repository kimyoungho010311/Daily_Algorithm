class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


tree = BinaryTree()

# 노드 저장할 딕셔너리
nodes = {}

# 노드 개수
t = int(input())

for _ in range(t):
    root, left, right = input().split()

    # 루트 노드 생성 (없으면)
    if root not in nodes:
        nodes[root] = Node(root)

    # 트리의 최상단 설정 (첫 입력이 루트라고 가정)
    if tree.root is None:
        tree.root = nodes[root]

    # 왼쪽 자식 처리
    if left != '.':
        if left not in nodes:
            nodes[left] = Node(left)
        nodes[root].left = nodes[left]

    # 오른쪽 자식 처리
    if right != '.':
        if right not in nodes:
            nodes[right] = Node(right)
        nodes[root].right = nodes[right]


def preorder(n):
    if n:
        print(n.item, end='')
        preorder(n.left)
        preorder(n.right)


def inorder(n):
    if n:
        inorder(n.left)
        print(n.item, end='')
        inorder(n.right)


def postorder(n):
    if n:
        postorder(n.left)
        postorder(n.right)
        print(n.item, end='')


preorder(tree.root)
print()
inorder(tree.root)
print()
postorder(tree.root)