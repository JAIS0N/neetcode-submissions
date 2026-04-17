class Solution:
    def maxArea(self, heights: List[int]):
        i=0
        j=len(heights)-1
        all=[]
        while j>i:
            area=(j - i) * min(heights[i], heights[j])
            all.append(area)
            if heights[i] < heights[j]:
                i=i+1
            else:
                j=j-1
        return max(all)

        