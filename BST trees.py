# O(h) - h-tree's height

class BST_Node:
    def __init__(self,key=None):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None

def find(root,key):
    while root is not None:
        if root.key==key:
            return root
        elif key<root.key:
            root=root.left
        else:
            root=root.right
    return

def smallest(node):
    while node.left:
        node=node.left
    return node

def largest(node):
    while node.right:
        node=node.rigth
    return node

def succ(node):
    if node.right:
        return smallest(node.right)
    y = node.parent
    while y and node == y.right:
        node = y
        y = y.parent
    return y

def pred(node):
    if node.left:
        return largest(node.left)
    y = node.parent
    while y and node == y.left:
        node = y
        y = y.parent
    return y

def insert(root,key):
    if not root.key:
        root.key = key
        return

    z = BST_Node(key)
    y = None
    x = root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if z.key < y.key:
        y.left = z
    else:
        y.right = z

def delete(d, key):
    root=find(d,key)

    if root.right is None and root.left is None:
        root.parent.right=None
        root.parent.left=None
    else:
        if (root.right is None or root.left is None) and\
                root.right.right is None and \
                root.right.left is None and \
                root.left.right is None and \
                root.left.left is None:
            if root.right:
                root.parent.right=root.right
            elif root.left:
                root.parent.left=root.left
        else:
            next=succ(root)
            next.parent.left=None
            root.key=next.key




T=[4,1,6,2,8,3,9,7]
d=BST_Node()
for t in T:
    insert(d,t)

delete(d,8)
if find(d,6).right:
    print(find(d,6).right.key)
else:
    print(None)


if find(d,9).left:
    print(find(d,9).left.key)
else:
    print(None)








