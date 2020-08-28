def solution(N):
    binary_value = bin(N)[2:]
    count = result = 0
    start = False
    
    for i in range(0,len(binary_value)):
        if binary_value[i] == '1':
            if count > result:
                result = count
                count = 0
            if start:
                count = 0
            else:
                start = True
        if start and (binary_value[i] == '0'):
            count = count + 1
    
    return result

def test(args, expect):
	print("Expect: " + str(expect) + ", was: " + str(solution(args)))

test(1041,5)
test(15,0)
test(10,1)
test(328, 2)