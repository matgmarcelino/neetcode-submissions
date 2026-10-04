class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1

        while (l < r) :
            l_char = s[l]
            r_char = s[r]

            if (not l_char.isalnum()) :
                l += 1
            elif (not r_char.isalnum()) :
                r -= 1
            elif (l_char != r_char) :
                return False
            else:
                l += 1
                r -= 1
        

        return True