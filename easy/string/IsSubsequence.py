"""
Given two string s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., 'ace' is a subsequence of 'abcde' while 'aec' is not).
"""

def isSubsequence(s: str, t: str) -> bool:
    # Empty string is always a subsequence
    if not s:
        return True
        
    if len(s) > len(t):
        return False
    
    pointer_s = 0
    pointer_t = 0

    while pointer_t < len(t) and pointer_s < len(s):
        if s[pointer_s] == t[pointer_t]:
            pointer_s += 1
        
        pointer_t += 1

    if pointer_s == len(s):
        return True
    else:
        return False


assert isSubsequence("abc", "ahbgdc") == True
assert isSubsequence("axc", "ahbgdc") == False
assert isSubsequence("", "ahbgdc") == True
assert isSubsequence("b", "abc") == True
