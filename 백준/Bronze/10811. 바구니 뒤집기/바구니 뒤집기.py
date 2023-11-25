import sys
n, m = map(int, sys.stdin.readline().split())
l = [i+1 for i in range(n)]
for index in range(m):
    i, j = map(int, sys.stdin.readline().split())
    num = (j-i+1)//2
    for k in range(num):
        s = l[i-1+k]
        l[i-1+k] = l[j-1-k]
        l[j-1-k] = s

print(" ".join(map(str,l)))
        
        