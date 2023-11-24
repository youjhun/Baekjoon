import sys
n, m = map(int,sys.stdin.readline().split())
l = [0 for i in range(n)]
for i in range(m):
    start, final, index = map(int,sys.stdin.readline().split())
    for j in range(start-1,final):
        l[j] = index

print(str(l)[1:-1].replace(",",""))