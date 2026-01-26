#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        countA = Counter(a)
        for i in b:
            if countA[i] > 0:
                countA[i] -= 1
            else:
                return False
        return True
    
    
    
