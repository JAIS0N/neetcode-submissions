class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n < 3:
            return 0

        i=0 
        j = n - 1
        left_max = 0
        right_max = 0
        water = 0

        while i<j:
            if height[i] < height[j]:
                if height[i] >= left_max:
                    left_max = height[i]
                else:
                    water += left_max - height[i]
                i += 1
            else:
                if height[j] >= right_max:
                    right_max = height[j]
                else:
                    water += right_max - height[j]
                j -= 1

        return water