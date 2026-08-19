class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current):

            # If we used every number,
            # we created one full permutation.
            if len(current) == len(nums):
                result.append(current[:])
                return

            # Try every number.
            for num in nums:

                # Do not use a number
                # that is already in current.
                if num in current:
                    continue

                # Take the number.
                current.append(num)

                # Continue building.
                backtrack(current)

                # Undo the choice.
                current.pop()

        backtrack([])

        return result