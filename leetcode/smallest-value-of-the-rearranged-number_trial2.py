class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        is_negative = num < 0
        s = str(abs(num))
        count = [0] * 10

        for char in s:
            count[int(char)] += 1
            
        res = []
        if is_negative:
            for d in range(9, -1, -1):
                res.append(str(d) * count[d])
            return -int("".join(res))
        
        else:
            for d in range(1, 10):
                if count[d] > 0:
                    res.append(str(d))
                    count[d] -= 1
                    break
            res.append('0' * count[0])
            
            for d in range(1, 10):
                res.append(str(d) * count[d])
                
            return int("".join(res))
    
