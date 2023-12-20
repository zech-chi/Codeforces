t = int(input())
for _ in range(t):
	arr = [0] * 26 
	n = int(input())
	mcl = input()
	for i in range(n):
		arr[ord(mcl[i]) - ord('A')] += 1
	
	count = 0
	for i in range(26):
		if arr[i] >= i + 1:
			count += 1
	print(count)
