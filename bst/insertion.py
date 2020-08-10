class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        node = Node(val)
        if (self.root is None):
            self.root = node
            return self.root
        else:
            node = self.root


        while(True):
            if (node.info > val and node.left is None):
                node.left = Node(val)
                break
            elif (node.info <= val and node.right is None):
                node.right = Node(val)
                break
            
            if(node.info > val):
                node = node.left
            else:
                node = node.right
        
        return self.root

tree = BinarySearchTree()
t = 6

arr = list(map(int, '4 2 3 1 7 6'.split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
