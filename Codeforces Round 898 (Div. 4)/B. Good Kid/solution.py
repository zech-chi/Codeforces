def read_int_list():
    return list(map(int, input().split()))

size = int(input(""))
res = []
for _ in range(size):
    arr_size = int(input(""))
    arr = read_int_list()
    Min = arr[0]
    indx = 0
    for i in range(1, arr_size):
        if arr[i] < Min:
            Min = arr[i]
            indx = i
    arr[indx] += 1
    p = 1
    for k in arr:
        p *= k
    res.append(p)
    
for i in range(size):
    print(res[i])
