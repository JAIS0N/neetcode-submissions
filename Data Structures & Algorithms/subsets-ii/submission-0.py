class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
       

        # Sort so duplicate numbers are next to each other.
        nums.sort()

        result = []

        def backtrack(start, current):

            # Every current combination is a valid subset.
            result.append(current[:])

            # Try each number from 'start'.
            for i in range(start, len(nums)):

                # Skip duplicate numbers at the same level.
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Take nums[i].
                current.append(nums[i])

                # Move forward.
                backtrack(i + 1, current)

                # Undo the choice.
                current.pop()

        backtrack(0, [])

        return result