class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l: int = 1
        r: int = max(piles)
        minK: int = r

        while l <= r:
            k: int = (l + r) // 2
            hours: int = 0
            for b in piles:
                hours += math.ceil(b / k)

            if hours <= h:
                minK = min(minK, k)
                r = k - 1
            else:
                l = k + 1

        return minK

        
