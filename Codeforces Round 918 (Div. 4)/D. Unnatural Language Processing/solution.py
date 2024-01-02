t = int(input())
C = {'b', 'c', 'd'}
V = {'a', 'e'}

for _ in range(t):
	n = int(input())
	s = list(input())
	l = 0
	for r in range(n):
		if r == n - 1:
			if l != 0:
				print(".", end="")
			print("".join(s[l:r + 1]))
		elif s[r] in V:
			pass
		elif s[r] in C and s[r + 1] in C:
			if l != 0:
				print(".", end="")
			print("".join(s[l:r + 1]), end="")
			l = r + 1
		elif s[r] in C and s[r + 1] in V:
			if l != 0 and l != r:
				print(".", end="")
			print("".join(s[l:r]), end="")
			l = r
