# CSES Problem Set
# Two Sets
# https://cses.fi/problemset/task/1092

from math import ceil, sqrt

n = int(input())

if n in {1, 2}: # Trivial cases
	print('NO')

else:
	if not (n + 1) % 4: # Median of (1, 2,..., n) divisible by 4 - passes
		print('YES')
		x = ceil((sqrt(2*n*(n+1)+1)-1)/2) # Lowest int such that sumToX >= (sumToN)/2

		# Determines integer to omit from lower set
		omit = x*(x+1)//2 - n*(n+1)//4 # TL: "sum to X, minus (sum to N)/2"

		if omit: # if sumToX exceeds half of sumToN - true for n > 3
			print(x-1) # One less in first set ('omit' will be skipped)
			for q in range(1, x+1):
				if q == omit:
					continue # skip 'omit' value
				print(q, end = ' ')
			print()

			print(n-x+1)
			print(omit, end = ' ')
			for r in range(x+1, n+1):
				print(r, end = ' ')

		# Only for n = 3; didn't want to hard-code it
		else: # if sumToX == sumToN
			print(x) # 'omit' remains in lower set
			for s in range(1,x+1):
				print(s, end = ' ')
			print()

			print(n-x)
			for t in range(x+1, n+1):
				print(t, end = ' ')

	elif not n % 4: # Divisible by 4 - passes
		print('YES')

		print(n//2)
		for i in range(1, n//4 + 1): # Numbers outside interquartile range
			print(f'{i} {n+1 - i}', end =' ')
		print()

		print(n//2)
		for j in range(n//4 + 1, n//2 + 1): # Numbers within interquartile range
			print(f'{j} {n + 1 - j}', end = ' ')
	else:
		print('NO')