from math import sqrt
t = int(input())

def is_perfect_square(n):
	q = int(sqrt(n))
	return (q * q == n)

for _ in range(t):
	n = int(input())
	Sum = sum(map(int, input().split()))
	if is_perfect_square(Sum):
		print("Yes")
	else:
		print("No")