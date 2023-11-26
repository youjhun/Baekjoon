import sys
ans = []
col = 0
row = 0
while True:
    try:
        s = list(sys.stdin.readline())
        s.remove("\n")
        ans.append(s)
        row += 1
        if col <= len(s):
            col = len(s)
    except:
        break
for i in range(col):
    for j in range(row):
        try:
            print(ans[j][i], end="")
        except:
            pass