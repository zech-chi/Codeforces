t = int(input(""))
res = []
for _ in range(t):
    n, k, x = map(int, input().split())
    if x == (n * (n + 1)) // 2:
        if k == n:
            res.append("Yes")
        else:
            res.append("No")

    elif x > (n * (n + 1)) // 2:
        res.append("No")

    elif (k * (k + 1)) // 2 > x:
        res.append("No")

    elif (k * (k + 1)) // 2 == x:
        res.append("Yes")
    
    else:
        diff_sum = ((n * (n + 1)) // 2) - x
        diff_rest = n - k
        s = 1
        while ((s * (s + 1)) // 2) <= diff_sum:
            s += 1
        s -= 1
        if diff_rest > s:
            res.append("No")
        else:
            res.append("Yes")

for r in res:
    print(r)
