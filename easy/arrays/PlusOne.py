def solution(digits):
    for i in range((len(digits) -1), -1, -1):
        currentDigit = digits[i] + 1

        if currentDigit < 10:
            digits[i] = currentDigit
            break
        else:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
    
    print digits


solution([1,2,3])
solution([1,9])
solution([9])
solution([9,9])