t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	arr = [i + 1 for i in range(n)]
	output = arr[n - k - 1:]
	output.extend(reversed(arr[:n - k - 1]))
	print(" ".join(map(str, output)))
