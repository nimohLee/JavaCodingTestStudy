from collections import deque

class Solution(object):
    def maxDepth(self, root):
        max_depth = 0
        if root is None:
            return max_depth
        q = deque()
        q.append((root, 1))
        while q:
              cur_node, cur_depth = q.popleft()
              max_depth = cur_depth

              if cur_node.left:
                  q.append(cur_node.left, cur_depth+1)
              
              if cur_node.right:
                  q.append(cur_node.right, cur_depth+1)
        
        return max_depth
