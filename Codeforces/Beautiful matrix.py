r, c = 0, 0
for row in range(5):
    line = list(map(int, input().split()))
    if 1 in line:
        r = row
        c = line.index(1)
moves = abs(r - 2) + abs(c - 2)
print(moves)