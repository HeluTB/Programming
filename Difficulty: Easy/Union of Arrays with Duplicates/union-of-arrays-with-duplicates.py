class Solution:    
    def findUnion(self, a, b):
        # code here
        joined_array = set(a)
        joined_array.update(b)
        return joined_array