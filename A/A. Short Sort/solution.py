n = int(input(""))
matrix = []
for i in range(n):
    s = input("")
    matrix.append(s)
for s in matrix:
    if s in {"abc", "acb", "bac", "cba"}:
        print("Yes")
    else:
        print("No")
