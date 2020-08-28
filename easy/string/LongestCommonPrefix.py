def longestCommonPrefix(strs) -> str:
    if len(strs)==0: return ""
    elif len(strs)==1: return strs[0]

    result = ""

    for a in range(len(min(strs))): 
        for b in range(1, len(strs)):
            if strs[0][a]==strs[b][a]:
                if b==len(strs)-1:
                    result += strs[0][a]
            else:
                return result
    return result

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["a"]))
