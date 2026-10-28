class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l: int = 0
        r: int = len(nums)

        while l < r:
            m: int = l + ((r - l) // 2)

            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        return l if l < len(nums) and nums[l] == target else -1




















# Left and right pointers.
# Calculate midpoint
# Update left and right pointers