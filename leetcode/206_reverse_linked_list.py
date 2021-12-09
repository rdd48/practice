# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        Verbose but slow solution for reversing a linked list.
        Runtime: 72 ms, faster than 5.12% of Python3 online submissions for Reverse Linked List.
        Memory Usage: 15.6 MB, less than 46.40% of Python3 online submissions for Reverse Linked List.
        """
        
        if not head:
            return None
        
        new_head = head.next
        head.next = None
        
        while new_head:
            curr_next = new_head.next
            new_head.next = head
            head = new_head
            new_head = curr_next
        
        return head