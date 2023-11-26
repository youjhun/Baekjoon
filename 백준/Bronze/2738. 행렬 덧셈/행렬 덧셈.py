import sys
n, m = map(int, sys.stdin.readline().split())

a=[]; b=[];
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    b.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
        if j != m-1:
            print(a[i][j],end =' ')
        else:
            print(a[i][j])