class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        pre: int = 1
        post: int = 1
        res: List[int] = [1] * n

        for i in range(n):
            res[i] *= pre
            pre *= nums[i]

        for i in range(n - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res
