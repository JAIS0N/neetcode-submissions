class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen=[]
        left=0
        right=len(numbers)-1
        while left<right:
            k=numbers[left]+numbers[right]
            if target==k:
                return [left+1,right+1]
            if target<k:
                right=right-1
            else:
                left=left+1
            
        