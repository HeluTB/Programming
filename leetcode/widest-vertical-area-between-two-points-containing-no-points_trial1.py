class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = [p[0] for p in points]
        n = len(x)
        x.sort()
        max_width = 0

        for i in range(n):
            width = x[i] - x[i - 1]
            if width > max_width:
                max_width = width
        
        return max_width