# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #0 -> 1 -> 2 -> 3 -> None
        #iterate throughout list

        #have prev = None, curr = head

        #while curr
            #save = curr.next
            #curr.next = prev
            #prev = curr
            #curr = save
        #return head

        prev, curr = None, head
        while curr:
            save = curr.next
            curr.next = prev
            prev = curr
            curr = save
        
        return prev
        