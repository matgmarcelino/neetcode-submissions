class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        running_sum, l = 0, 0, 
        for r in range(len(nums)):
            running_sum += nums[r]

            while l <= r and running_sum >= target:
                res = min(res, (r - l) + 1)
                running_sum -= nums[l]
                l += 1
        
        return 0 if res == float('inf') else res