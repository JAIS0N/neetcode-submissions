from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        output = []
        q = deque()   # stores indices
        l = 0
        
        for r in range(len(nums)):
            
            # 1. Remove smaller elements from back
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # 2. Add current index
            q.append(r)
            
            # 3. Remove left element if it is outside window
            if q[0] < l:
                q.popleft()
            
            # 4. When window size reaches k
            if (r - l + 1) == k:
                output.append(nums[q[0]])  # max is at front
                l += 1   # slide window
        
        return output