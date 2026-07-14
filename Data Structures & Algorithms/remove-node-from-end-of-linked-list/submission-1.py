# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        p = 1
        while(curr.next):
            p += 1
            curr = curr.next
        m = p - n
        print(m)
        if m == 0:
            return head.next
        i = 0
        curr = head
        while(curr.next):
            if i == m - 1:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next
            i += 1
        return head
            