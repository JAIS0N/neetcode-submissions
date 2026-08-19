class Node:
    def __init__(self, key, value):
        # Store the key
        self.key = key

        # Store the value
        self.value = value

        # Previous node
        self.prev = None

        # Next node
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        # Maximum number of items allowed
        self.capacity = capacity

        # Dictionary:
        # key -> Node
        self.cache = {}

        # Dummy left node represents the LRU side
        self.left = Node(0, 0)

        # Dummy right node represents the most recently used side
        self.right = Node(0, 0)

        # Connect dummy nodes
        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        # Get the nodes before and after this node
        prev_node = node.prev
        next_node = node.next

        # Connect them together
        # This removes node from the list
        prev_node.next = next_node
        next_node.prev = prev_node


    def insert(self, node):
        # We always insert near the right side
        # because right means most recently used

        # Get the node currently before right
        prev_node = self.right.prev

        # Connect previous node to new node
        prev_node.next = node

        # Connect new node back to previous node
        node.prev = prev_node

        # Connect new node to right
        node.next = self.right

        # Connect right back to new node
        self.right.prev = node


    def get(self, key: int) -> int:

        # If key does not exist
        if key not in self.cache:
            return -1

        # Get the node from dictionary
        node = self.cache[key]

        # Since we just used this node,
        # it becomes most recently used.
        self.remove(node)
        self.insert(node)

        # Return its value
        return node.value


    def put(self, key: int, value: int) -> None:

        # If key already exists
        if key in self.cache:

            # Get old node
            old_node = self.cache[key]

            # Remove old node from linked list
            self.remove(old_node)

        # Create a new node
        new_node = Node(key, value)

        # Store it in dictionary
        self.cache[key] = new_node

        # Put it at the most recently used side
        self.insert(new_node)

        # If cache became too large
        if len(self.cache) > self.capacity:

            # First real node after left
            # is the least recently used node
            lru = self.left.next

            # Remove it from linked list
            self.remove(lru)

            # Remove it from dictionary
            del self.cache[lru.key]