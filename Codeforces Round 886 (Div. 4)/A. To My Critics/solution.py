t = int(input())

for _ in range(t):
	a, b, c = map(int, input().split())
	if a + b >= 10 or a + c >= 10 or b + c >= 10:
		print("Yes")
	else:
		print("No")