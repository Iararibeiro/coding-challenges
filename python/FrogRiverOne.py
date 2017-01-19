# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    aux = set(A)
    leaf_number = 0
    position = -1
    
    for i in range(0, len(A)):
        if leaf_number < X:
            if A[i] in aux:
                aux.remove(A[i])
                leaf_number = leaf_number + 1
                if X == leaf_number:
                    position = i
    return position
    
    