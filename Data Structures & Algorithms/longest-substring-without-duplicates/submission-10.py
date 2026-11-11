class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res: int = 0
        window: set[str] = set()
        l: int = 0

        for r in range(len(s)):
            char: str = s[r]

            while char in window:
                window.remove(s[l])
                l += 1
            
            window.add(char)
            res = max(res, r - l + 1)
        
        return res
