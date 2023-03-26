def traversal(root):
    if root is None:
        return
    traversal(root.left)
    traversal(root.right)