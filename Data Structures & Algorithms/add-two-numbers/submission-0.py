# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)

        curr = l1
        cur = l2
        main = dummy
        carry = 0

        while (curr or cur or carry):
            val1 = curr.val if curr else 0
            val2 = cur.val if cur else 0 
            total = val1 + val2 + carry
            carry = total // 10
            main.next = ListNode(total % 10)
            main = main.next
            curr = curr.next if curr else None
            cur = cur.next if cur else None
        return dummy.next