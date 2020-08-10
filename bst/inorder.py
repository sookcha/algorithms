"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    if root.left != None:
        inOrder(root.left)
    print(root, end=' ')
    if root.right != None:
        inOrder(root.right)
