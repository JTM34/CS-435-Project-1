class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def insertRec(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                insertRec(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insertRec(root.right, node)

def sort(root):
    if not root:
        return
    sort(root.left)
    print root.data
    sort(root.right)
	
r = Node(3)
insertRec(r, Node(7))
insertRec(r, Node(1))
insertRec(r, Node(5))
insertRec(r, Node(17))
insertRec(r, Node(12))
insertRec(r, Node(53))

print "in order:"
sort(r)