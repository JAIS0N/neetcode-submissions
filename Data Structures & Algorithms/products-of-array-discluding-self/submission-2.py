class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        for i in range(len(nums)):
            prod=1
            for j in range(len(nums)):
                if j==i:
                    continue
                prod=prod*nums[j]
            ans[i]=prod
        return ans
            
        