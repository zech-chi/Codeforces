t = int(input())

for _ in range(t):
	n = int(input())
	index = 1
	hight = -1
	for i in range(n):
		a, b = map(int, input().split())
		if a <= 10:
			if hight < b:
				index = i + 1
				hight = b
	print(index)