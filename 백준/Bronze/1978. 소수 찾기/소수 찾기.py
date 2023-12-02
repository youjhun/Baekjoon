import sys
n = int(input())
p = list(map(int, sys.stdin.readline().split()))
cnt = 0
for num in p:
    mark = 1
    if num == 1:
        continue
    for i in range(2,num):
        if num%i==0:
            mark = 0
    if mark:
        cnt += 1
print(cnt)