class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l: int = 0
        r: int = len(heights) - 1
        res: int = 0

        while (l < r):
            area: int = (min(heights[r], heights[l]) * (r - l))
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res