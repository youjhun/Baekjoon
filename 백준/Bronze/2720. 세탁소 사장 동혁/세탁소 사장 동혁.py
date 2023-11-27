n = int(input())
money = [25,10,5,1]
for i in range(n):
    ans = []
    m = int(input())
    for j in money:
        # print(j)
        if m//j != 0:
            ans.append(str(m//j))
            m = m%j
        else:
            ans.append(str(0))
    print(" ".join(ans))