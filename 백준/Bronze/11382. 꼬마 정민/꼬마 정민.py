import sys
num = list(map(int, sys.stdin.readline().split()))
ans = 0 
for i in num:
    ans += i
print(ans)