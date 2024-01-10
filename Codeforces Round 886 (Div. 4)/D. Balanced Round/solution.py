t = int(input())

for _ in range(t):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	arr.sort()
	dp = [1]
	for i in range(1, n):
		if abs(arr[i] - arr[i - 1]) <= k:
			dp.append(1)
		else:
			dp.append(0)
			dp.append(1)

	consective_ones = 0
	count = 0
	for i in range(len(dp)):
		if dp[i] == 1:
			count += 1
		else:
			consective_ones = max(consective_ones, count)
			count = 0
	consective_ones = max(consective_ones, count)
	print(n - consective_ones)