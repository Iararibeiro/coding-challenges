"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters and
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

def isPalindrome(s: str) -> bool:
    # Convert string to list of lowercase alphanumeric characters
    cleaned = [char.lower() for char in s if char.isalnum()]
    
    # Compare characters from start and end moving towards center
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True


assert isPalindrome("A man, a plan, a canal: Panama") == True

assert isPalindrome("race a car") == False

assert isPalindrome(" ") == True