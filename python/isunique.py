def solution(word):
	occurency = [False] * 26
	result = True

	for letter in word:
		position= ord(letter) - ord('a')
		if occurency[position] == False:
			occurency[position] = True
		else:
			result = False

	return result

print solution("abca")
print solution("abc")

