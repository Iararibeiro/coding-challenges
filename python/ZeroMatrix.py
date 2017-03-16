# code for exercise 1.8 - Zero Matrix from the book Craking the Code Interview
# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, 
# its entire row and column are set to 0.
#
# Author: Iara Ribeiro - March/2017

def solution(A):
	actual_col = None
	actual_row = None

	for i in range(0,len(A)):
		for j in range(0,len(A[i])):
			if A[i][j] == 0:
				if actual_col == None:
					actual_col = j
					actual_row = i
					A = nullify_col(A,j)
					A = nullify_row(A,i)
				elif actual_col != j and actual_row != i:
					actual_col = j
					actual_row = i
					A = nullify_col(A,j)
					A = nullify_row(A,i)

	return A

def nullify_col(A,j):
	for i in range(0,len(A)):
		A[i][j] = 0

	return A

def nullify_row(A,i):
	A[i] = [0 for x in range(0,len(A[i]))]
	return A


def test(args1,expect):
	print(str(expect) == str(solution(args1)))
	print("Expect: " + str(expect) + ", was: " + str(solution(args1)))

test([[1,1,0],[1,1,1],[0,1,1]],[[0,0,0],[0,1,0],[0,0,0]])
test([[1,0],[1,1]],[[0,0],[1,0]])
test([[1,0,1],[1,1,1]],[[0,0,0],[1,0,1]])
