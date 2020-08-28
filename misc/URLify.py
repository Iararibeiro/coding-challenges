def solution(word):
	size = len(word) -1
	result = ""
	free_spaces = 0
	letter = False

	for char in range(size,-1,-1):
		if word[char]==" " and not letter:
			free_spaces += 1
		elif word[char]==" " and letter and free_spaces > 0:
			free_spaces -= 2
			result = "%20" + result
		else:
			letter = True
			result = word[char] + result
 
	return result

print solution("Mr John Smith    ")
print solution("116   ")
print solution("1 4 6")
print solution(" ")
