class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        max_area = 0
        a = 0
        while i < j:
            if height[i] > height[j]:
                a = height[j] * (j - i)
                j -= 1
            else:
                a = height[i] * (j - i)
                i += 1
            max_area = max(max_area, a)
        return max_area