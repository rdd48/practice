# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # thanks badrabbit for the code this is based on

        remainder = 0
        lout = None

        while l1 or l2 or remainder:

            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            val = (val1 + val2 + remainder) % 10
            remainder = (val1 + val2 + remainder) // 10
        
            if not lout:
                lout = ListNode(val)
                lout_head = lout
                # lout_copy = lout
                # lout_tail = lout
            else:
                next_node = ListNode(val)
                lout.next = next_node
                lout = lout.next
                # lout_tail.next = ListNode(val)
                # lout_tail = lout_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return lout_head