def solution(word):
	occurency = [False] * (25)
	result = True

	for letter in word:
		position= ord(letter) - 97
		if occurency[position] == False:
			occurency[position] = True
		else:
			result = False

	return result

print solution("abc")
print solution("casa")
#print solution("116")
#print solution("146")

