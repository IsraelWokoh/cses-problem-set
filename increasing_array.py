# CSES Problem Set
# Increasing Array
# https://cses.fi/problemset/task/1094

n = int(input())
nums = list(map(int, input().split()))
moves = 0

for x in range(len(nums) - 1):
	if nums[x] > nums[x + 1]:
		diff = nums[x] - nums[x + 1]
		moves += diff
		nums[x+1] += diff
print(moves)