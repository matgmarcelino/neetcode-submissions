class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count: Dict[str, int] = defaultdict(int)
        most_freq: int = 0
        res: int = 0
        l: int = 0
        for r in range(len(s)):
            count[s[r]] += 1
            most_freq = max(most_freq, count[s[r]])

            while (r - l + 1) - most_freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
