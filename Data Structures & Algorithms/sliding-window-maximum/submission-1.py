class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res: List[int] = []
        q: deque[int] = deque()

        l: int = 0
        r: int = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1
        
        return res

























# remove all items smaller than num at r from right of queue
# append num at r into q
# if biggest number is out of bounds, remove
# if window is of size k, append to res and increment left pointer
            




