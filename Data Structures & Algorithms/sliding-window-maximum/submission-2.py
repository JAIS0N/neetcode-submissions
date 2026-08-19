class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Stores indexes of useful numbers.
        # The biggest value will always be at the front.
        dq = deque()

        # Store maximum of each window.
        result = []

        for right in range(len(nums)):

            # Remove smaller values from the back.
            # They cannot become maximum because
            # the current value is bigger and newer.
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # Add current index.
            dq.append(right)

            # Left side of the current window.
            left = right - k + 1

            # If the front index is outside the window,
            # remove it.
            if dq[0] < left:
                dq.popleft()

            # Once we have a full window,
            # the front contains the maximum.
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result