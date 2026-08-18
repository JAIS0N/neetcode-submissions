# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node helps us easily build the answer linked list.
        dummy = ListNode(0)

        # current points to the last node in our answer.
        current = dummy

        # Stores carry from addition.
        # Example: 8 + 7 = 15
        # We store 5 and carry 1.
        carry = 0

        # Continue while l1 or l2 has nodes,
        # or we still have a carry left.
        while l1 or l2 or carry:

            # Get value from l1.
            # If l1 is finished, use 0.
            val1 = l1.val if l1 else 0

            # Get value from l2.
            # If l2 is finished, use 0.
            val2 = l2.val if l2 else 0

            # Add both digits and previous carry.
            total = val1 + val2 + carry

            # Carry is everything in the tens place.
            carry = total // 10

            # Current digit is the ones place.
            digit = total % 10

            # Create a new node with this digit.
            current.next = ListNode(digit)

            # Move current forward.
            current = current.next

            # Move l1 forward if possible.
            if l1:
                l1 = l1.next

            # Move l2 forward if possible.
            if l2:
                l2 = l2.next

        # dummy was only a helper node.
        # The real answer starts at dummy.next.
        return dummy.next