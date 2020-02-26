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
                root.left.parent = root
                
            else:
                insertRec(root.left, node)
        else:
            if root.right is None:
                root.right = node
                root.right.parent = root
            else:
                insertRec(root.right, node)


def findMinRec(node):
    curr = node
    
    while(curr.left is not None):
        curr = curr.left
      
    print curr.data

def findMaxRec(node):
    curr = node
    
    while(curr.right is not None):
        curr = curr.right
      
    print curr.data

	
r = Node(3)
insertRec(r, Node(7))
insertRec(r, Node(1))
insertRec(r, Node(5))
insertRec(r, Node(17))
insertRec(r, Node(12))
insertRec(r, Node(53))

print "min"
findMinRec(r)

print "max"
findMaxRec(r)
