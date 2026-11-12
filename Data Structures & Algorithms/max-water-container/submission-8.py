class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res: int = 0
        l: int = 0
        r: int = len(heights) - 1

        while l < r:
            area: int = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res