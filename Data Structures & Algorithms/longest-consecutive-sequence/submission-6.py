

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Put all numbers into a set (O(n)) for O(1) lookups
        s = set(nums)
        longest = 0

        # Loop through each number in the set
        for x in s:
            # Only start counting if x is the BEGINNING of a streak
            # (i.e., x-1 is not in the set)
            if x - 1 not in s:
                y = x       # start walking forward
                length = 1  # current streak length is at least 1

                # Keep moving forward as long as consecutive numbers exist
                while y + 1 in s:
                    y += 1
                    length += 1

                # Update the longest streak found so far
                longest = max(longest, length)

        # Return the length of the longest consecutive sequence
        return longest
