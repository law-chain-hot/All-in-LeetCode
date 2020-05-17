# 101. Symmetric Tree

"""
# { 2020.05.14 } 
# { Method 1: Recursively }
# { Method 2: Iteratively }  ??
# { Optimal: Method 1 2 }
    - Time complexity:   O(n)
    - Space complexity:  O(n) 

# { My own explanation of this problem }


    # Iterative 的方法，你要看看
        # 有点厉害，用的是传统的 BFS ，但是一次 pop 2 个数
        # 同时，按照下面的顺序 append
            t1.left  
            t2.right  
            t1.right  
            t2.left 


"""


class Solution:
    def isSymmetric(self, root: TreeNode):
        if not root:
            return True
        return self.isEqual(root.left, root.right)
        
        
    def isEqual(self, root1, root2):
        # check if both are none
        if root1 == None and root2 == None:
            return True
        
        # check if one of both is wrong
        if root1 == None or root2 == None:
            return False
        
        equal = self.isEqual(root1.left, root2.right) and self.isEqual(root1.right, root2.left) and root1.val == root2.val
        
        return equal