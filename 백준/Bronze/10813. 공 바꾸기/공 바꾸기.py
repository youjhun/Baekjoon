import sys
n, m = map(int, sys.stdin.readline().split())
l = [i+1 for i in range(n)]
for index in range(m):
    i, j = map(int, sys.stdin.readline().split())
    k = l[i-1]
    l[i-1] = l[j-1]
    l[j-1] = k
for item in l:
    print(item, end = " ")

