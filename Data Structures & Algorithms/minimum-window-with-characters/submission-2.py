class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        window: dict[str, int] = defaultdict(int)
        countT: dict[str, int] = defaultdict(int)

        for ch in t: 
            countT[ch] += 1

        need: int = len(countT)
        have: int = 0

        res: List[int] = [-1, -1]
        resLen: int = -1

        l: int = 0
        for r in range(len(s)):
            c: str = s[r]
            window[c] += 1
            
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if resLen == -1 or (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                ch: str = s[l]
                window[ch] -= 1
                if ch in countT and window[ch] < countT[ch]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != -1 else ""
            

            
            

