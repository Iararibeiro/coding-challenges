#MaxCounters with 60% of rate

def solution(N, A):
    counters = list([0] * N)
    
    for k in range(0, len(A)):
        if A[k] == (N + 1) :
            counters = [max(counters)] * N
        else:
            for x in range(1,N):
                if A[k] == (x) :
                    counters[(x-1)] = counters[(x-1)] + 1 
    
    return counters