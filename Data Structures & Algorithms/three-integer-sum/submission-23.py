class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res: List[List[int]] = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            l: int = i + 1
            r: int = len(nums) - 1

            while l < r:
                summed: int = nums[i] + nums[l] + nums[r]

                if summed > 0:
                    r -= 1
                    continue
                if summed < 0:
                    l += 1
                    continue

                while l < r and nums[l] == nums[l + 1]:
                    l += 1

                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
        
        return res
