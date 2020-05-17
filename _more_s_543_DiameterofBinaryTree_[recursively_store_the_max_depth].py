# 543. Diameter of Binary Tree

"""
# { 2020.05.14   2 } 
# { Method 1: Recursively }
# { Optimal: Method 1 }
    - Time complexity:   O(n)
    - Space complexity:  O(n) 

# { My own explanation of this problem }


Store the max of left depth + right depth


"""




class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        def calDiam(root):
            # base case
            if not root:
                return 0
            left = calDiam(root.left)
            right = calDiam(root.right)
            self.diameter = max(left+right, self.diameter)
            return max(left, right) + 1
        
        calDiam(root)  
        
        return self.diameter 