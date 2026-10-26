class Solution:
    def trap(self, height: List[int]) -> int:
        res: int = 0
        l: int = 0
        r: int = len(height) - 1
        maxl: int = height[l]
        maxr: int = height[r]

        while (l < r):
            if height[l] <= height[r]:
                maxl = max(maxl, height[l])
                res += maxl - height[l]
                l += 1
            else:
                maxr = max(maxr, height[r])
                res += maxr - height[r]
                r -= 1

        return res