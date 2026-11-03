class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res: List[int] = []
        q: deque[int] = deque()
        l: int = 0
        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if (r - l + 1) >= k:
                res.append(nums[q[0]])

                if nums[q[0]] == nums[l]:
                    q.popleft()
                l += 1
                

        return res