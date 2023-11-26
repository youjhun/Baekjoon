import sys
index = 1
store = 0
ans = ""
while True:
    try:
        row = list(map(int, sys.stdin.readline().split()))
        if store <= max(row):
            ans = ""
            store = max(row)
            ans = str(index) + " " + str(row.index(store)+1)
        index += 1
    except:
        break
print(store)
print(ans)