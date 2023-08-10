# CSES Problem Set
# Creating Strings
# https://cses.fi/problemset/task/1622

from functools import reduce
from itertools import permutations as perms
from operator import mul

def fact(num):
	if num in {0,1}:
		return 1
	return reduce(mul, (i for i in range(2,num+1)), 1)

n = input()
maximum = fact(len(n))
for char in set(letter for letter in n):
	rep = n.count(char)
	if rep > 1 :
		maximum//=fact(rep)
print(maximum)

for perm in set(perms(char for char in sorted(n))):
	print(''.join(perm))