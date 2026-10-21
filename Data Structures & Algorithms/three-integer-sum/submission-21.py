class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n: int = len(nums) - 1
        res: List[List[int]] = []

        for i in range(n + 1):
            if nums[i] > 0: break
            if i > 0 and nums[i - 1] == nums[i]: continue

            l: int = i + 1
            r: int = n
            while (l < r):
                summed: int = nums[l] + nums[r] + nums[i]

                if summed > 0:
                    r -= 1
                    continue

                if summed < 0:
                    l += 1
                    continue

                res.append([nums[i], nums[l], nums[r]])
                
                l += 1
                r -= 1

                while l < r and nums[l - 1] == nums[l]:
                    l += 1
                
        return res

                
            