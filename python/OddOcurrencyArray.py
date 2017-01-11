def solution(A):
	return reduce(lambda x, y: x^y, A)
    

def test(args1,expect):
	print("Expect: " + str(expect) + ", was: " + str(solution(args1)))

test([9,3,9,3,9,7,9],7)
