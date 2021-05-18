# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# take01 97%
class Solution:
    def real_val(self, l):
        return l.val if l is not None else 0
        
    def real_next(self, l):
        return l if l is None else l.next  

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode() 
        next_one = l3 
        while True:
            tmp_val = self.real_val(l1) + self.real_val(l2) + next_one.val
            if tmp_val>=10:
                tmp_val = tmp_val % 10
                up_val = 1
            else:
                up_val = 0 
            next_one.val = tmp_val
            if up_val == 1 or self.real_next(l1) is not None or self.real_next(l2) is not None:
                next_one.next = ListNode(up_val)
                next_one = next_one.next 
                l1 = self.real_next(l1)
                l2 = self.real_next(l2)
            else:
                break
        return l3 