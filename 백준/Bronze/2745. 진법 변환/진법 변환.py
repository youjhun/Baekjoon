import sys
ans = 0
index = 1
n, b = map(str, sys.stdin.readline().split())
l = reversed(list(n))
for item in l:
    if item.isalpha():
        ans += (ord(item) - 55) * index
    else:
        ans += int(item) * index
    index *= int(b)
print(ans)