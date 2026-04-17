class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()                # store unique triplets as tuples

        for i in range(n):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:   # skip duplicate 'a'
                continue

            seen = set()           # values seen while scanning for this 'a'
            target = -a
            for j in range(i + 1, n):
                need = target - nums[j]
                if need in seen:
                    # (a <= need <= nums[j]) because array is sorted and 'need' came from earlier j
                    res.add((a, need, nums[j]))
                seen.add(nums[j])

        return [list(t) for t in res]


        