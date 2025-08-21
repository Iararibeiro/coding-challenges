"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating 
order, starting with word1. If a string is longer than the other, append the additional letters 
onto the end of the merged string.

Return the merged string.
"""

def mergeAlternately(word1: str, word2: str) -> str:
    pointer_word1, pointer_word2 = 0, 0
    res = ""

    while pointer_word1 < len(word1) or pointer_word2 < len(word2):
        if pointer_word1 < len(word1):
            res += word1[pointer_word1]

        if pointer_word2 < len(word2):
            res += word2[pointer_word2]

        pointer_word1 += 1
        pointer_word2 += 1
        
    return res


assert mergeAlternately("abc", "pqr") == "apbqcr"
assert mergeAlternately("ab", "pqrs") == "apbqrs"
assert mergeAlternately("abcd", "pq") == "apbqcd"