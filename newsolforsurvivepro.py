t = int(input())

for testcase in range(t):
	n,k,s = map(int, input().split())

	work_days = s - (s//7)
	total_consumption = k*s//n

	if (work_days < total_consumption):
		print(-1)


	else:
		print(total_consumption)
	