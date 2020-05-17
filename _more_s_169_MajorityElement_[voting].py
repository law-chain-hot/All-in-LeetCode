"""
# { 2020.05.13 }
# { Method: 2 } 
# { Hash Table or Voting }
# { Optimal: Voting }  ？Not yet 
    - Time complexity:   O(n)
    - Space complexity:  O(1) 

# { My own explanation of this problem }




"""




import collections

# Hash Table
class Solution:
    def majorityElement(self, nums):
        threshold = math.floor(len(nums)/2)
        count = {}
        for num in nums:
            if not count.get(num):
                count[num] = 1
            else:
                count[num] += 1
            if count[num] > threshold:
                return num
        return None



# Hash Table [Offical]
def majorityElement(nums):
    counts = collections.Counter(nums)
    print(counts)
    return max(counts.keys(), key=counts.get)


test = [3,2,3,1,2,12,321,312,3,21,1,31,3,3]
print(majorityElement(test))