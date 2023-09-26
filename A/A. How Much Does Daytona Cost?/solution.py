t = int(input(""))
ans = []
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    founded = False
    for i in range(n):
        if arr[i] == k:
            founded = True
            break
    
    if founded:
        ans.append("Yes")
    else:
        ans.append("No")

for a in ans:
    print(a)
