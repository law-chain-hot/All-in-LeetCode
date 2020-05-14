# 283. Move Zeros [none-zero-position]

"""
# { 2020.05.13 } 
# { Method 1: Record all 0 and del them later }
# { Method 2: Record the position of nonZero }
# { Optimal: Method 2 }
    - Time complexity:   O(n)
    - Space complexity:  O(1) 

# { My own explanation of this problem }





"""






# optimal
# in-place
def moveZeroes(self, nums):
    nonZeroPos = 0  # records the position of nonZero
    for i in xrange(len(nums)):
        if nums[i] != 0:
            nums[i], nums[nonZeroPos] = nums[nonZeroPos], nums[i]
            nonZeroPos += 1