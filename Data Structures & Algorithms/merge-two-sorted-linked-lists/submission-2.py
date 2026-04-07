# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #linked1 (1 -> 2 -> 4)
        #linked2 (1 -> 3 -> 5)
        dummy = newList = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            
            dummy = dummy.next

        if list1:
            dummy.next = list1
        else:
            dummy.next = list2
        
        return newList.next

        #while link1 and link2:
            #if val link1 < val link2:
                #dummy.next = val link1
                #link1 = link1.next
            #else:
                #dummy.next = val link2
                #
            
            #dummmy = dummy.next