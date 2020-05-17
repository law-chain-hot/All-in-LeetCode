# 437. Path Sum III

"""
# { 2020.05.15 } 
# { Method 1: Brute force }
# { Method 2: space time Trade Off } optimal
# { Optimal: Method 2 }
    - Time complexity:   O(n)
    - Space complexity:  O(n) 

# { My own explanation of this problem }


暴力： 写 2 个 helper function

最优： it is a typical [space and time trade off]
        用一个 dictionary 
            key：前路sum
            val：出现的次数

"""



# brute froce 
class Solution:
    # brute froce 
    def pathSum(self, root: TreeNode, target: int):
        self.pathNum = 0
        self.bfs(root, target)
        return self.pathNum
    
    
    def bfs(self, root, target):
        if not root:
            return 
        self.checkSum(root, target)
        self.bfs(root.left, target)
        self.bfs(root.right, target)
        
    
    def checkSum(self, root, target):
        if not root:
            return 
        if root.val == target:
            self.pathNum += 1
        self.checkSum(root.left, target - root.val)
        self.checkSum(root.right, target - root.val)
    
    
    
    

# Memorization of path sum
class Solution:
    # Memorization of path sum
    def pathSum(self, root: TreeNode, target: int):
        # cache is used for counting the num of each path sum that appears
        cache = {}
        cache[0] = 1
        
        self.numOfPath = 0
        
        self.bfs(root, target, 0, cache)
        
        return self.numOfPath
        
    def bfs(self, root, target, currPathSum, cache):
        # base case
        if not root:
            return
        # get current pathSum
        currPathSum += root.val
        # get the sum from self.cache
        cachedPathSum = currPathSum - target
        
        # update
        # check if cache has the corresponding value 
        self.numOfPath += cache.get(cachedPathSum, 0)
        # cache the count of sum
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # def breakdown
        self.bfs(root.left, target, currPathSum, cache)
        self.bfs(root.right, target, currPathSum, cache)
        # del 1 count when change branch
        cache[currPathSum] -= 1
    
    
    
    
    