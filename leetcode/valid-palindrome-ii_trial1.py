class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1

        while l < r:
            if s[l] != s[r]:
                lskip = s[l + 1: r + 1] 
                rskip = s[l: r]

                return lskip == lskip[:: -1] or rskip == rskip[:: -1]
            
            l += 1
            r -= 1
        
        return True