# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        
        while head.next is not None:
            head = head.next
            num = (num * 2) + head.val
        
        return num

        # my first attempt, not knowing binary conversions
#         str_val = str(head.val)
        
#         while head.next is not None:
#             head = head.next
#             str_val += str(head.val)
        
#         return int(str_val, 2)