def traversal(root):
    if root is None:
        return
    traversal(root.left)
    traversal(root.right)

def preOrder(root):
    visited = []
    if root is None:
        return
    visited.append(root.value)
    traversal(root.left)
    traversal(root.right)

def inOrder(root):
    visited = []
    if root is None:
        return
  
    traversal(root.left)
    visited.append(root.value)
    traversal(root.right)    

def postOrder(root):
    visited = []
    if root is None:
        return
  
    traversal(root.left)
    traversal(root.right)    
    visited.append(root.value)