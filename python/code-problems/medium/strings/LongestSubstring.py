def lengthOfLongestSubstring(s: str) -> int:
    result = ""
    print(len(s))
    for i in range(0, len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if isUnique(substring) and len(substring) > len(result):
                result = substring

    return len(result)

def isUnique(word: str) -> bool:
    if len(word) > 26: return False

    letters = [0] * 26

    for letter in word:
        position = ord(letter) - 97
        if letters[position]:
            return False
        else:
            letters[position] = True

    return True

def OptLengthOfLongestSubstring(s: str) -> int:
    dic = {}
    windowSize = 0
    start = -1
    end = 0

    for i,char in enumerate(s):
        end = i
        lastPosition = dic.get(char, None)

        if lastPosition != None and lastPosition > start:
            start = lastPosition

        currentWindow = end - start
        windowSize = max(windowSize, currentWindow)
        dic[char] = i
    return windowSize

#lengthOfLongestSubstring("abcabcbb")
OptLengthOfLongestSubstring("abcabcbb")
#lengthOfLongestSubstring("bbbbb")
OptLengthOfLongestSubstring("bbbbb")
#lengthOfLongestSubstring("pwwkew")
OptLengthOfLongestSubstring("pwwkew")
#lengthOfLongestSubstring("au")
OptLengthOfLongestSubstring("au")
