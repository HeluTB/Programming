class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        x = max(piles)
        freq = [0] * (x + 1)
        total = 0
        count = 0
        needed = n // 3

        for p in piles:
            freq[p] += 1
        
        alice_turn = True
        for i in range(x, -1, -1):
            while freq[i] > 0:
                if alice_turn:
                    alice_turn = False
                else:
                    total += i
                    count += 1
                    alice_turn = True

                freq[i] -= 1
                if count == needed:
                    return total

        return total   