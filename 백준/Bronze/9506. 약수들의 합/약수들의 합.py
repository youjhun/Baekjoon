while True:
    n = int(input())
    if n == -1:
        break
    s = []
    for i in range(1,n):
        if n%i == 0:
            s.append(i)
    if sum(s) == n:
        ans = f"{n} = 1"
        s.remove(1)
        for i in s:
            ans = ans + f" + {i}"
        print(ans)
    else:
        print(f"{n} is NOT perfect.")