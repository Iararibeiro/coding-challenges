def strStr(haystack, needle):
    if len(needle) > len(haystack): return -1

    result = -1

    i = 0
    j = 0
    count = 0
    while j < len(needle) and i < len(haystack):
        if haystack[i] != needle[j]:
            count += 1
            i = count
            j = 0
        else:
            j += 1
            i += 1

    if count == len(haystack): return 0
    return count

strStr("hello","ll")
print("#######")
strStr("aaaaa", "bba")
