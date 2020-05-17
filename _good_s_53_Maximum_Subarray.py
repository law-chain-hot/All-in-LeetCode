# 53. Maximum Subarray

"""
{ Pattern: Sliding window }

# { 2020.05.15 } 
# { Method 1: one pointer }
# { Optimal: Method 1 }
    - Time complexity:   O(n)
    - Space complexity:  O(1) 

# { My own explanation of this problem }





"""



class Solution:
    def maxSubArray(self, nums: List[int]):
        maxSum = -float('inf')
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum > maxSum:
                maxSum = currSum
            if currSum < 0:
                currSum = 0
                
        return maxSum