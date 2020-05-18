# 581. Shortest Unsorted Continuous Subarray

"""
# { 2020.05.18 } 
# { Method 1: Sort }
    - Time complexity:   O(n*logn)
    - Space complexity:  O(n) 
# { Optimal: stack }
    - Time complexity:   O(n)
    - Space complexity:  O(n or 1) 

# { My own explanation of this problem }


用 sort 很直白

之后再看 stack 的情况

"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]):
        # edge case
        if len(nums) <= 1:
            return 0
        
        # sort
        sortNums = nums.copy()
        sortNums.sort()
        left = float('inf')
        right = 0
        for i in range(len(nums)):
            if nums[i] > sortNums[i]:
                left = min(left, i)
            elif nums[i] < sortNums[i]:
                right = max(right, i)
        
        if left == float('inf'):
            return 0
        else:
            return right - left + 1