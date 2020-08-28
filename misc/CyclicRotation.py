def solution(A,K):
    result = [0 for i in range(len(A))] 

    if len(A) > 1:
        if K > len(A):
            K = K%len(A)

        for i in range(0,len(A)):
            index = i + K
            if index < len(A):
                result[index] = A[i]
            else:
                index = index - len(A)
                result[index] = A[i]
    else:
        result = A

    return result

def test(args1,args2,expect):
	print("Expect: " + str(expect) + ", was: " + str(solution(args1,args2)))

test([3,8,9,7,6],3,[9,7,6,3,8])
test([5],3,[5])
test([3,8,9],5,[8,9,3])
test([3,8,9],6,[3,8,9])
test([],3,[])