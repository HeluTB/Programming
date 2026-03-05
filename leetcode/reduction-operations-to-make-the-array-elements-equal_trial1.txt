class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        total = 0
        up = 0

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up += 1
            total += up
        
        return total
        