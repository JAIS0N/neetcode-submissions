class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
         # Min heap stores:
        # (distance, x, y)
        heap = []

        # Put every point into the heap
        for x, y in points:

            # Distance from origin without sqrt
            distance = x * x + y * y

            # Add point with its distance
            heapq.heappush(heap, (distance, x, y))

        result = []

        # Take the closest point k times
        for _ in range(k):

            # Smallest distance comes out first
            distance, x, y = heapq.heappop(heap)

            # Add the point to answer
            result.append([x, y])

        return result