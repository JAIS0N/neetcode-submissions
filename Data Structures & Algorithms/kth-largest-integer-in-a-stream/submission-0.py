
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        # Store k
        self.k = k

        # This heap will keep only the largest k numbers
        self.heap = []

        # Add every starting number
        for num in nums:

            # Put number into heap
            heapq.heappush(self.heap, num)

            # If heap has more than k numbers,
            # remove the smallest number
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)


    def add(self, val: int) -> int:

        # Add new value to heap
        heapq.heappush(self.heap, val)

        # Keep only k largest numbers
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Smallest number among the k largest
        # is the kth largest number
        return self.heap[0]