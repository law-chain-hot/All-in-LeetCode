"""
# { 2020.05.13 }
# { Method: 2 } 
# { Recursively or Iteratively }
# { Optimal: Iteratively }
    - Time complexity:   O(n)
    - Space complexity:  O(1) 

# { My own explanation of this problem }




"""





# ============================================================
# Iteratively   
"""
- Time complexity:   O(n)
- Space complexity:  O(1) 
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while(curr != None):
            curr.next, curr, prev = prev, curr.next, curr
        
        return prev




# ============================================================
# Recursively
"""
- Time complexity:   O(n)
- Space complexity:  O(n) 
"""
class Solution:
    def reverseList(self, head: ListNode):
        if not head or not head.next:
            return head
        lastNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return lastNode
        
        
