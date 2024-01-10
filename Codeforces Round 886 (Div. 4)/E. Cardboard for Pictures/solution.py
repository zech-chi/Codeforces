import math
t = int(input())

for _ in range(t):
	n, C = map(int, input().split())
	S = list(map(int, input().split()))
	a = 0
	b = 0
	c = 0
	for s in S:
		a += 4
		b += 4 * s
		c += s ** 2
	
	delta = b ** 2 - 4 * a * (c - C)
	w = int((-b + math.sqrt(delta)) / (2*a))

	print(w)
