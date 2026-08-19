class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        # Go through every number
        for num in nums:

            # Add number to heap
            heapq.heappush(heap, num)

            # Keep only k largest numbers
            if len(heap) > k:
                heapq.heappop(heap)

        # Smallest among the k largest
        # is the kth largest
        return heap[0]