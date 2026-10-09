class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, running_sum, l = 0, 0, 0
        for r in range(len(nums)):
            running_sum += nums[r]
            if res == 0 and running_sum >= target:
                res = (r - l) + 1

            while l <= r and running_sum >= target:
                res = min(res, (r - l) + 1)
                running_sum -= nums[l]
                l += 1
        
        return res