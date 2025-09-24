import random
from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def preorder(root):
    if root:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=' ')

def level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        n = q.popleft()
        print(n.key, end=' ')
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)


def delete_node(root, key):
    if not root:
        return None
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if not root.left: return root.right
        if not root.right: return root.left
        temp = root.right
        while temp.left:
            temp = temp.left
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)
    return root


nums = [random.randint(1, 1000) for _ in range(100)]

root = None
for n in nums:
    root = insert(root, n)

print("Altura:", height(root))

print("\nPré-ordem:"); preorder(root)
print("\nIn-order:"); inorder(root)
print("\nPós-ordem:"); postorder(root)
print("\nEm nível:"); level_order(root)

print("\n\n--- Deletando raiz ---")
root = delete_node(root, root.key)
level_order(root)

if root.left:
    print("\n--- Deletando raiz da subárvore esquerda ---")
    root = delete_node(root, root.left.key)
    level_order(root)

if root.right:
    print("\n--- Deletando raiz da subárvore direita ---")
    root = delete_node(root, root.right.key)
    level_order(root)
