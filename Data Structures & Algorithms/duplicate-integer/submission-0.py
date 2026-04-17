class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
    # Use a set to store the unique values
        seen = set()
        
        # Iterate through each number in the array
        for num in nums:
            # If the number is already in the set, return True
            if num in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(num)
        
        # If no duplicates are found, return False
        return False

    # Example usage:
    # nums = [1, 2, 3, 1]
    # print(containsDuplicate(nums))  # Output: True

    # nums = [1, 2, 3, 4]
    # print(containsDuplicate(nums))  # Output: False

            