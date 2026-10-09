class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        running_sum, l = 0, 0, 
        for r in range(n):
            running_sum += nums[r]

            while l <= r and running_sum >= target:
                res = min(res, (r - l) + 1)
                running_sum -= nums[l]
                l += 1
        
        return 0 if res > n else res