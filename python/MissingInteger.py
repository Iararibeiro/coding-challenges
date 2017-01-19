def solution(A):
    def solution(A):
    occurrence = [False] * (len(A) + 1)
    for item in A:
        if 1 <= item <= len(A) + 1:
            occurrence[item-1] = True
 
    # Find out the missing minimal positive integer.
    for index in xrange(len(A) + 1):
        if occurrence[index] == False:
            return index + 1
 
    raise Exception("Should never be here.")
    return -1