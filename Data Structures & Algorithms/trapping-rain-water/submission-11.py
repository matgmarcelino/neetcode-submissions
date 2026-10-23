class Solution:
    def trap(self, height: List[int]) -> int:
        res: int = 0
        l: int = 0
        r: int = len(height) - 1
        maxl: int = height[l]
        maxr: int = height[r]

        while (l < r):
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                res += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                res += maxr - height[r]

        return res

            