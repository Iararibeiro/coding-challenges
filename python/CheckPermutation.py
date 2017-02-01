def solution(A,B):
	if len(A) == len(B):
		sumA = 0
		sumB = 0
		for char in range(0,len(A)):
			sumA += ord(A[char])
			sumB += ord(B[char])

		if sumA == sumB:
			return True
		else:
			return False
	else:
		return False

print solution("dog","god")
print solution("123","321")
print solution("123","32 1")
print solution("3","1")
print solution("1","1")
