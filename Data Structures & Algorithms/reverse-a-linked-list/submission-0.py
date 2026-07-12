# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while(curr is not None):
            arr.append(curr.val)
            curr = curr.next
        dummy = ListNode(-1)
        curr = dummy
        for val in arr[::-1]:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next
