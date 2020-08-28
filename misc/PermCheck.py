# this solution was right, but didint pass in the performance test

def solution(A):
    N = len(A)
    result = 1
    num = 1

    if N < max(A):
        return 0
    
    for i in range(0,N):
        try:
            if min(A) == num :
                A.remove(min(A))
                num = num + 1
        except ValueError:
            "is not a permutation"
    
    if len(A) > 0 :
        return 0
    else:
        return result

#this function scored 100%, the function set eliminates duplicates

def solution2(A):
    if max(A)!=len(A) or len(set(A))!=len(A):
        return 0
    return 1