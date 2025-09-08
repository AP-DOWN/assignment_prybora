#9910
a, b = map(int, input().split())
l = min(a, b) + 1
r = max(a, b) - 1
count = 0
for x in range(l, r + 1):
    if x % 2 != 0:
        count += 1
print(count)

