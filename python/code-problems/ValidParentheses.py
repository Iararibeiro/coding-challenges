def validParentheses(s) -> str:
    if len(s)%2 == 1: return False
    if len(s) == 0: return True

    stack = []

    for el in s:
        if el == '(' or el == '{' or el == '[':
            stack.append(el)
        else:
            if (len(stack) > 0):
                last = stack.pop()
                if el == ')' and last != '(' or el == '}' and last != '{' or el == ']' and last != '[':
                    return False

    return len(stack) == 0


print(validParentheses("()")) #true
print(validParentheses("()[]{}")) #true
print(validParentheses("(]")) #false
print(validParentheses("([)]")) #false
print(validParentheses("{[]}")) #true
print(validParentheses("{{}[][[[]]]}")) #true
