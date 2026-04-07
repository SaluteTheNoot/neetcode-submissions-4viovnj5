# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #just thinking about it, you would have an array like:
            # 0 -> 1 -> 2 -> 3 -> None
        #you would need to iterate through this array, prev and curr
            #have 
        curr = head
        prev = None

        while curr:
            hold = curr.next
            curr.next = prev
            prev = curr
            curr = hold
        return prev