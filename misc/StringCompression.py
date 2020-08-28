def solution(string):
    result = ""
    count = 0
    letter = string[0]

    for index in range(0, len(string)):
        if letter == string[index]:
            count += 1
        else:
            result = result + letter + str(count)
            count = 1
            letter = string[index]

    result = result + letter + str(count)

    if len(result) >= len(string):
        return string
        
    return result

def test(args1, expect):
    print("Expect: " + str(expect) + ", was: " + str(solution(args1)))

test("aabcccccaaa","a2b1c5a3")
test("abcdefghij", "abcdefghij")
