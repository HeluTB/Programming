class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, h = 0, n
    
        while l <= h:
            mid = (l + h) // 2
            needed = mid * (mid + 1) // 2
            
            if needed == n:
                return mid
            elif needed < n:
                l = mid + 1
            else:
                h = mid - 1
                
        return h