# 104. Maximum Depth of Binary Tree

"""
# { My own explanation of this problem }
# { 2020.05.13 }
# { Method: 2 } 
# { Recursion or BFS }

We can traverse the tree with recursion

At every step, we will call the original function twice 
with the left child and right child, respectively.

And we get the maximum depth of them, then the value should 
be added 1 when it is returned.

Finally, the base case is if the root node doesn't exist, we just return 0
"""



"""
Complexity Analysis
    - Time complexity : O(m). 
        A total of mm nodes need to be traversed. Here, m represents the number of nodes from the given tree.

    - Space complexity : O(m) 
        The depth of the recursion tree can go upto m in the case of a skewed tree. In average case, depth will be O(logm)
"""



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recurison
class Solution:
    def maxDepth(self, root: TreeNode):
        
        # base case 
        if not root:
            return 0
        
        depthLeft = self.maxDepth(root.left)    
        depthRight = self.maxDepth(root.right)
            
        depth = max(depthLeft, depthRight) + 1
        
        return depth



# BFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        level = [root] if root else []
        print(level)
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
            
        return depth


root = TreeNode()

s = Solution()
s.maxDepth(root)

