class Solution:
    def trap(self, height: List[int]) -> int:
        l: int = 0
        r: int = len(height) - 1
        maxLeft: int = height[l]
        maxRight: int = height[r]
        res: int = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]

        return res