n, total = map(int, input().split())
a = list(map(int, input().split()))
count = 0
cur_time = 0
i = 0

for j in range(n):
    cur_time += a[j]
    while cur_time > total:
        cur_time -= a[i]
        i += 1
    
    count = max(count, j - i + 1)

print(count)