# 21. Merge Two Sorted Lists

"""
# { 2020.05.14 } 
# { Method 1: Recursively }
# { Method 2: Iteratively } concise
# { Optimal: Method 2 }
    - Time complexity:   O(n+m)
    - Space complexity:  O(1) 

# { My own explanation of this problem }





"""




# Recursively
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        curr = ListNode(0)
        dummy = curr
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2
        
        return dummy.next





# Iteratively
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):        
        # base case
        if not l1 or not l2:
            return l1 or l2
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2