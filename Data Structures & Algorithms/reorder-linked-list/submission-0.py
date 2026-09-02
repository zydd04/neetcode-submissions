# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        arr = []

        while(curr):
            arr.append(curr)
            curr = curr.next
        
        curr = ListNode(0)
        l = 0
        r = len(arr) - 1
        for i in range(len(arr)):
            if i % 2 == 0:
                curr.next = arr[l]
                print(f"{arr[l]}")
                l += 1
            else:
                curr.next = arr[r]
                print(f"{arr[r]}")
                r -= 1
            curr = curr.next
        curr.next = None

        
                
                    

                    
                    
            
        
        

