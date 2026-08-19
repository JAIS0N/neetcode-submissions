class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
     
        # Start both pointers from the first value.
        slow = nums[0]
        fast = nums[0]

        # First step:
        # Find where slow and fast meet inside the cycle.
        while True:

            # Slow moves one step.
            slow = nums[slow]

            # Fast moves two steps.
            fast = nums[nums[fast]]

            # They meet somewhere inside the cycle.
            if slow == fast:
                break

        # Start slow again from the beginning.
        slow = nums[0]

        # Move both one step at a time.
        # The place where they meet is the duplicate number.
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow