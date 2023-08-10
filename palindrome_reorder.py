# CSES Problem Set
# Palindrome Reorder
# https://cses.fi/problemset/task/1755

def find(string):
	odd = 0 # number of character with odd number of appearances
	evenLetter = dict() # chars with even occurrences
	oddLetter = tuple() # either empty or two-element

	for char in set(letter for letter in string):
		charCount = string.count(char)
		if not charCount % 2: # if even number of occurrences
			evenLetter[char] = charCount
		else:
			odd += 1 # increments odd based on parity
			if odd > 1: # can't have palindrome with >1 odd-occurrence letters
				return 'NO SOLUTION'
			oddLetter = (char, charCount)

	palindrome = ''
	for letter, counter in evenLetter.items(): # prints half, in order
		palindrome += letter*(counter//2)
	if odd: # odd letter in the middle
		palindrome += oddLetter[0]*oddLetter[1]
	for letter, counter in reversed(evenLetter.items()): # print second half, in reverse order
		palindrome += letter*(counter // 2)
	return palindrome

print(find(input()))