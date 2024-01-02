t = int(input())

for _ in range(t):
	matrix = []
	for _ in range(3):
		matrix.append(input())

	for r in range(3):
		for c in range(3):
			if matrix[r][c] == '?':
				if c == 0:
					if matrix[r][1] in {'A', 'B'} and matrix[r][2] in {'A', 'B'}:
						print("C")
					elif matrix[r][1] in {'A', 'C'} and matrix[r][2] in {'A', 'C'}:
						print("B")
					else:
						print("A")
				if c == 1:
					if matrix[r][0] in {'A', 'B'} and matrix[r][2] in {'A', 'B'}:
						print("C")
					elif matrix[r][0] in {'A', 'C'} and matrix[r][2] in {'A', 'C'}:
						print("B")
					else:
						print("A")
				if c == 2:
					if matrix[r][0] in {'A', 'B'} and matrix[r][1] in {'A', 'B'}:
						print("C")
					elif matrix[r][0] in {'A', 'C'} and matrix[r][1] in {'A', 'C'}:
						print("B")
					else:
						print("A")