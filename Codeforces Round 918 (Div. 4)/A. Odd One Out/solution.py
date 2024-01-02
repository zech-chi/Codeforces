t = int(input())

for _ in range(t):
	x, y, z = map(int, input().split())
	print(x ^ y ^ z)
