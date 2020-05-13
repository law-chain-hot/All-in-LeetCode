# 104. Maximum Depth of Binary Tree

"""
# { 2020.05.13 }
# { Method: 2 } 
# { HashTable or Math!!! }
# { Optimal: Math }
    - Time complexity:   O(n)
    - Space complexity:  O(n) 

# { My own explanation of this problem }






"""




# My suboptimal
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if not dic.get(num):
                dic[num] = 1
            else:
                dic.pop(num)
        for key in dic.keys():
            return key



# Optimal (Math)
# 2*(a+b+c)−(a+a+b+b+c)=c
class Solution:
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)





"""
{official}

We use hash table to avoid the O(n) time required for 
searching the elements in the list

Iterate through all elements in nums and set up key/value 
pair.

Return the element which appeared only once.

"""