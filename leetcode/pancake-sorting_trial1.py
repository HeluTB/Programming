class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        k_vals = []
        for i in range(n, 1, -1):
            idx = arr.index(i)
            if idx == i - 1:
                continue
            
            if idx != 0:
                k_vals.append(idx + 1)
                arr[:idx + 1] = arr[:idx + 1][::-1]
            
            k_vals.append(i)
            arr[:i] = arr[:i][::-1]
        
        return k_vals            