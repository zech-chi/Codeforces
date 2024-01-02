t = int(input())

for _ in range(t):
	A, B, C = 0, 0, 0
	for _ in range(3):
		for i in input():
			if i == 'A':
				A += 1
			elif i == 'B':
				B += 1
			else:
				C += 1
	
	if A != 3:
		print("A")
	elif B != 3:
		print("B")
	else:
		print("C")
