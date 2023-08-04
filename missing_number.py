# CSES Problem Set
# Missing Number
# https://cses.fi/problemset/task/1083

n = int(input())
oneToN = set(map(int, input().split()))

for i in range(1, n+1):
	if i not in oneToN:
		print(i)