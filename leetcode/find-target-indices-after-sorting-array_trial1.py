class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller_count = 0
        count = 0
        
        for num in nums:
            if num < target:
                smaller_count += 1
            elif num == target:
                count += 1

        result = []
        for i in range(count):
            result.append(smaller_count + i)
            
        return result