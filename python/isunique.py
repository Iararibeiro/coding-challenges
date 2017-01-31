def solution(word):
	occurency = [False] * (127-32)
	result = True

	for letter in word:
		position= ord(letter) - 32
		if occurency[position] == False:
			occurency[position] = True
		else:
			result = False

	return result

print solution("abca")
print solution("116")
print solution("146")

