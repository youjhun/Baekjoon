import sys
cnt = 0
n = int(input())
a = [[0 for i in range(1000)] for j in range(1000)]
for index in range(n):
    l,u = map(int, sys.stdin.readline().split())
    for i in range(l,l+10):
        for j in range(u, u+10):
            a[i][j] = 1

for item in a:
    cnt += item.count(1)
print(cnt)