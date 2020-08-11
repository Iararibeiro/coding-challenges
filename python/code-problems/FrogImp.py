import math

def solution(X, Y, D):
    A = (Y-X)
    A = (math.ceil(float(A)/float(D)))
    return int(A)

