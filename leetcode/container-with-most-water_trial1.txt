class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        max_area = 0
        area = 0
        while i < j:
            if height[i] > height[j]:
                area = height[j] * (j - i)
                j -= 1
            else:
                area = height[i] * (j - i)
                i += 1
            max_area = max(max_area, area)
        
        return max_area