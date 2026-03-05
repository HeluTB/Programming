import sys
inputs = sys.stdin.read().split()
n = int(inputs[0])
a = list(map(int, inputs[1:]))

odds = False
evens = False

for i in a:
    if i % 2 == 0:
        evens = True
    else:
        odds = True

if odds and evens:
    a.sort()

print(*a)