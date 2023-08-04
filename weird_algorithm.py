# CSES Problem Set
# Weird Algorithm
# https://cses.fi/problemset/task/1068

number = int(input())
line = f'{number} '

while number > 1:
	if not number % 2:
		number //= 2
	else:
		number = 3 * number + 1
	line += f'{number} '
print(line.strip())