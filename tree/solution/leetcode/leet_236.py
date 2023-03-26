# Definition for a binary tree node.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        
        left = lowestCommonAncestor(root.left,p,q)
        right = lowestCommonAncestor(root.right,p,q)

        if root == p or root == q:
            return root
        elif left and right:
            return root
        return left or right