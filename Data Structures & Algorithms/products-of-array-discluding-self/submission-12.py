class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        pre: List[int] = [0] * n
        post: List[int] = [0] * n
        res: List[int] = [0] * n

        pre[0] = 1
        for i, num in enumerate(nums):
            if i == 0: continue
            pre[i] = pre[i - 1] * nums[i - 1]

        post[n - 1] = 1
        for i, num in reversed(list(enumerate(nums))):
            if i == n - 1: continue
            post[i] = post[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = pre[i] * post[i]

        return res

        