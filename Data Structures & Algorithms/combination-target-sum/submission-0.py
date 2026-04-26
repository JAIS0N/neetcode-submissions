class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, remaining: int, path: List[int]) -> None:
            # Found a valid combination
            if remaining == 0:
                result.append(path[:])   # store a copy
                return

            # Current sum exceeded target
            if remaining < 0:
                return

            # Try each candidate from 'start' onward
            for i in range(start, len(nums)):
                path.append(nums[i])                       # choose
                backtrack(i, remaining - nums[i], path)   # explore i+1 if unique pair no reuse
                path.pop()                                # unchoose

        backtrack(0, target, [])
        return result
        