# CSES Problem Set
# Permutations
# https://cses.fi/problemset/task/1070

line = ''
n = int(input())

def delta(numbers):
	pass

if n == 1:
	print(1)

elif n < 4:
	print('NO SOLUTION')

else:
	for x in range(2,n+1,2):
		print(f'{x} ', end='')

	for x in range(1,n+1,2):
		print(f'{x} ', end='')
