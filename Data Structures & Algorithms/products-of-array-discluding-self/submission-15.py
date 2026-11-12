class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        res: List[int] = [0] * n
        pre: List[int] = [0] * n 
        post: List[int] = [0] * n

        pre[0] = 1
        for i in range(1, n):
            pre[i] = nums[i - 1] * pre[i - 1]

        post[n - 1] = 1
        for i in range(n - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]
        
        for i in range(n):
            res[i] = pre[i] * post[i]

        return res