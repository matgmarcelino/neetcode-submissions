class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        res: List[int] = [-1, -1]
        resLen: int = -1
        window: dict[str, int] = defaultdict(int)
        countT: dict[str, int] = defaultdict(int)

        for c in t:
            countT[c] += 1

        need: int = len(countT)
        have: int = 0
        l: int = 0
        for r in range(len(s)):
            ch: str = s[r]
            window[ch] += 1
            if window[ch] == countT[ch]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen or resLen == -1:
                    resLen = r - l + 1
                    res = [l, r + 1]

                c: str = s[l]
                window[c] -= 1
                l += 1
                
                if window[c] + 1 == countT[c]:
                    have -= 1

        return "" if resLen == -1 else s[res[0] : res[1]]



            