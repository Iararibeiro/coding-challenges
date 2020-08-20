def isPalindrome(self, x: int) -> bool:
    if x < 0: return False

    #convert to string
    strNumber = str(x)
    reverse = ""

    for number in str(x):
        reverse = number + reverse

    if int(reverse) == x:
        return True

    return False

print isPalindrome(121)
print isPalindrome(-121)
print isPalindrome(10)
