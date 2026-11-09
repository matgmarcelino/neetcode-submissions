class Solution:
    def findMin(self, nums: List[int]) -> int:
        minN: int = nums[0]
        l: int = 0
        r: int = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                minN = min(minN, nums[l])
                break

            m: int = (r + l) // 2
            minN = min(minN, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return minN
            