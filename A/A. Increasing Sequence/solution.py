test_case_size = int(input(""))
res = []
for _ in range(test_case_size):
    arr_size = int(input(""))
    arr = list(map(int, input().split()))
    if arr[0] != 1:
        n = 1
    else:
        n = arr[0] + 1

    for i in range(1, arr_size):
        if n + 1 != arr[i]:
            n += 1
        else:
            n = arr[i] + 1
    res.append(n)

for n in res:
    print(n)
