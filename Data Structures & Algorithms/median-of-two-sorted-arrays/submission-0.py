class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Make sure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            # partition1 = how many elements nums1 gives to left side
            partition1 = (left + right) // 2

            # partition2 = how many elements nums2 gives to left side
            partition2 = (m + n + 1) // 2 - partition1

            # Boundary values for nums1
            maxLeft1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float("inf") if partition1 == m else nums1[partition1]

            # Boundary values for nums2
            maxLeft2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float("inf") if partition2 == n else nums2[partition2]

            # Correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                # Even total length
                if (m + n) % 2 == 0:
                    left_max = max(maxLeft1, maxLeft2)
                    right_min = min(minRight1, minRight2)
                    return (left_max + right_min) / 2

                # Odd total length
                return max(maxLeft1, maxLeft2)

            # We took too many elements from nums1
            elif maxLeft1 > minRight2:
                right = partition1 - 1

            # We took too few elements from nums1
            else:
                left = partition1 + 1
        