def lengthOfLongestSubstring(s):
    result = ""

    for i in range(0, len(s)):
        candidate = s[i]s

        for j in range(i+1, len(s)):
            #print (s[j])
            #print(s[j] in candidate)
            if s[j] in candidate:
                break
            else: 
                candidate = candidate + s[j]
        
        if len(candidate) > len(result):
            result = candidate

    return len(result)

lengthOfLongestSubstring("abcabcbb")
#OptLengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("bbbbb")
#OptLengthOfLongestSubstring("bbbbb")
lengthOfLongestSubstring("pwwkew")
#OptLengthOfLongestSubstring("pwwkew")
lengthOfLongestSubstring("au")
#OptLengthOfLongestSubstring("au")
