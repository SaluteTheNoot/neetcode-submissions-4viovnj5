class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Use an array to store nodes (not values)
        array1 = []
        curr = head
        while curr:
            array1.append(curr)  # Store the node itself
            curr = curr.next

        l, r = 0, len(array1) - 1

        # Reorder the list
        while l < r:
            array1[l].next = array1[r]  # Point lth node to rth node
            l += 1
            if l < r:  # Avoid self-linking in case of odd-length lists
                array1[r].next = array1[l]  # Point rth node to (l+1)th node
            r -= 1

        # Ensure the final node points to None
        array1[l].next = None
