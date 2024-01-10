t = int(input())

for _ in range(t):
	matrix = []
	for _ in range(8):
		line = input()
		row = []
		for c in line:
			row.append(c)
		matrix.append(row)
	word = []
	for r in range(8):
		for c in range(8):
			if matrix[r][c] != '.':
				word.append(matrix[r][c])
	print("".join(word))
	
