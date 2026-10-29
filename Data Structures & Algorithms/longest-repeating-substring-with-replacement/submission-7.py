class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res: int = 0
        count: dict[str, int] = defaultdict(int)
        most_freq: int = 0
        
        l: int = 0
        for r in range(len(s)):
            ch: str = s[r]
            count[ch] += 1
            if most_freq < count[ch]:
                most_freq = count[ch]

            
            while (r - l + 1) - most_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res
        
        
