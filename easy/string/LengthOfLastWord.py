def solution(s):
    solutionArray = []
    currentWord = ""

    for i in range(0, len(s)):
        if s[i] == " ":
            if len(currentWord) > 0 :
                solutionArray.append(currentWord)
                currentWord = ""
        else:
            currentWord += s[i]
    
    if len(currentWord) > 0 :
        solutionArray.append(currentWord)

    lastWord = solutionArray[len(solutionArray) - 1]

    return len(lastWord)



print(solution("Hello World"))
print(solution("   fly me   to   the moon  "))
print(solution("luffy is still joyboy"))
