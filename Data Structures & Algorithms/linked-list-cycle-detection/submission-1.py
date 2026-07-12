# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = set()
        while(head is not None and curr.next is not None):
            if curr.val not in seen:
                seen.add(curr.val)
            else:
                return True
            curr = curr.next

        return False