#9910
a, b = map(int, input().split())
left = min(a, b) + 1
right = max(a, b) - 1
count = (right + 1) // 2 - (left) // 2
print(count)
