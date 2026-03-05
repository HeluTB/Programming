class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        
        my_set = set(nums)
        my_set.remove(max(my_set))
        my_set.remove(max(my_set))

        return max(my_set)