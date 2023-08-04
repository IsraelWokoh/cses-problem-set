# CSES Problem Set
# Repetitions
# https://cses.fi/problemset/task/1069

string = input()
most = 1
current = 1
length = len(string)

if length in {0,1}:
	print(length)

else:
	for char in range(length - 1):
		if string[char] == string[char+1]:
			current += 1
			if current > most:
				most = current
		else:
			current = 1

	print(most)