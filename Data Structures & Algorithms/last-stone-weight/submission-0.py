class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
 
        # Convert stones into negative values
        # so Python's min heap behaves like a max heap.
        heap = [-stone for stone in stones]

        # Turn the list into a heap.
        heapq.heapify(heap)

        # Continue until 0 or 1 stone is left.
        while len(heap) > 1:

            # Get the heaviest stone.
            y = -heapq.heappop(heap)

            # Get the second heaviest stone.
            x = -heapq.heappop(heap)

            # If they are different,
            # put the remaining weight back.
            if y != x:
                heapq.heappush(heap, -(y - x))

        # If one stone remains, return it.
        # Otherwise return 0.
        return -heap[0] if heap else 0