class Solution:
    def isPalindrome(self, s: str) -> bool:
        l: int = 0
        r: int = len(s) - 1
        while l < r:
            l_char: str = s[l]
            if not str.isalnum(l_char):
                l += 1
                continue
            
            r_char: str = s[r]
            if not str.isalnum(r_char):
                r -= 1
                continue

            if l_char.lower() != r_char.lower():
                return False

            l += 1
            r -= 1

        return True

        
