class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 0
        end = n - 1
        for i in range(start, end):
            swapped = False
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
            
            end -= 1
            swapped = False
            for k in range(end - 1, start - 1, -1):
                if nums[k] > nums[k + 1]:
                    nums[k], nums[k + 1] = nums[k + 1], nums[k]
                    swapped = True
            start += 1