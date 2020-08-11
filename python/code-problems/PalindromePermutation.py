def solution(word):
	letters = {}
	result = True

	for letter in range(0, len(word)):
		#ord(letter)
		if 32 < ord(word[letter]) and ord(word[letter]) < 127:
			if word[letter] in letters:
				letters[word[letter]] += 1
			else:
				letters[word[letter]] = 1

	for key in letters.keys():
		if letters[key] % 2 > 0:
			result = False

	return result
	

print solution("dog god")
print solution("roma amor")
print solution("taco cat")
print solution("rome amor")
print solution("tacot cat")
