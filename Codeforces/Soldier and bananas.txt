k, n, w = map(int, input().split())
total = 0
for i in range(1, w + 1):
    total += i * k
if total - n > 0:
    print(total - n)
else: 
    print(0)