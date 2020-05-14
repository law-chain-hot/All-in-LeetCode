# 104. Maximum Depth of Binary Tree

"""
# { 2020.05.13 } 
# { Method 1: Singularity }
# { Optimal: Method 1 }
    - Time complexity:   O(n)
    - Space complexity:  O(1)   that is important, no extra space is used

# { My own explanation of this problem }


        # For each number i in nums,
        # we mark the number that (index i) points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number


At the same time, we use absolute function to make sure 
that the absolute values are equal

So there are still some positive number, they are what we need


"""







# 奇技淫巧 Singularity
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:   
        for i in range(len(nums)):
            # abs is used in case of nums(i) has been converted to negative
            index = abs(nums[i]) - 1 
            nums[index] = -abs(nums[index])
        
        # caution: this is called single line for loop in Python
        return [i+1 for i in range(len(nums)) if nums[i] > 0]