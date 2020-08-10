"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def postOrder(root):
    if root.left != None:
        postOrder(root.left)
    if root.right != None:
        postOrder(root.right)
    print(root, end=' ')
