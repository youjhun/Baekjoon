import sys
n, b = map(int, sys.stdin.readline().split())
num = []
q = n
while q != 0:
    r = q % b
    if r < 10:
        num.append(str(r))
    else:
        num.append(chr(r+55))
    q = q//b

num = "".join(reversed(num))
print(num)