# CSES Problem Set
# Number Spiral
# https://cses.fi/problemset/task/1071

for i in range(1,int(input())+1):
	row, col = map(int,input().split())
	m = max(row, col)
	diag = m**2 - (m - 1)

	if col == row: # On the diagonal
		print(diag)
	else:
		diff = abs(col - row)
		if m % 2: # Increasing RIGHT, then UP
			if col > row:
				print(diag + diff)
			else:
				print(diag - diff)

		else: # Increasing DOWN, then LEFT
			if row > col:
				print(diag + diff)
			else:
				print(diag - diff)
