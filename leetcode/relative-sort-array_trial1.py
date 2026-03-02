class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = len(arr1)
        count = [0] * 1001
        for x in arr1:
            count[x] += 1
        
        res = []
        for x in arr2:
            while count[x] > 0:
                res.append(x)
                count[x] -= 1
        
        m = len(count)
        for i in range(m):
            while count[i] > 0:
                res.append(i)
                count[i] -= 1
        
        return res
