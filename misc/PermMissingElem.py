def solution(A):
    n = ((len(A)+2)*(len(A)+1))/2 # sum of a perm number 1 to N
    
    for i in range(0,len(A)):
        n = n - A[i]
        
    return n