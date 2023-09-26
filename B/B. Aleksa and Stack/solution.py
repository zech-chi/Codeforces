t = int(input(""))
res = []
for _ in range(t):
    n = int(input(""))
    arr = [1, 3]
    for _ in range(2, n):
        a = arr[-1] + 1
        while (3 * a) % (arr[-1] + arr[-2]) == 0:
            a += 1
        arr.append(a)
    res.append(" ".join(map(str, arr)))
 
for r in res:
    print(r)
