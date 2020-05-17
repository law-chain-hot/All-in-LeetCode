# 234. Palindrome Linked List

"""
# { 2020.05.17 } 
# { Method 1: Double pointer }
# { Optimal: Method 1 }
    - Time complexity:   O(n)
    - Space complexity:  O(1) 

# { My own explanation of this problem }


Using double pointer to reverse the right half linked list
就是这一步非常关键
    # 找 middle node 的边界条件
    # 如何 reverse linked list

"""


class Solution:
    def isPalindrome(self, head: ListNode):        
        quickPtr = slowPtr = head
        while quickPtr and quickPtr.next:
            slowPtr = slowPtr.next
            quickPtr = quickPtr.next.next
        
        # get the middle node
        currPtr = slowPtr
        prevPtr = None
        
        # reverse the right part
        while currPtr:
            currPtr.next, currPtr, prevPtr = prevPtr, currPtr.next, currPtr
        
        # check if they 2 list are exactly same
        while prevPtr:
            if prevPtr.val != head.val:
                return False
            prevPtr = prevPtr.next
            head = head.next
            
        return True