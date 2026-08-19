"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


        # If the list is empty, return None.
        if not head:
            return None

        # Dictionary:
        # original node -> copied node
        copies = {}

        current = head

        # First pass:
        # Create a new copy of every node.
        while current:

            # Create a completely new node
            # with the same value.
            copies[current] = Node(current.val)

            # Move to the next original node.
            current = current.next

        # Start again from the beginning.
        current = head

        # Second pass:
        # Connect next and random pointers.
        while current:

            # Get the copied version
            # of the current node.
            copy = copies[current]

            # If current.next exists,
            # connect copy.next to its copied version.
            if current.next:
                copy.next = copies[current.next]

            # If current.random exists,
            # connect copy.random to its copied version.
            if current.random:
                copy.random = copies[current.random]

            # Move forward.
            current = current.next

        # Return the copied version of head.
        return copies[head]