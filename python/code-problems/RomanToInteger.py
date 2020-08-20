def romanToInt(s: str) -> int:
roman_values = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
value = 0

for i in range(len(s)):
    digit = s[i]
    value += roman_values[digit]
    if i > 0 and roman_values[s[i-1]] < roman_values[s[i]]:
        value = value - 2*roman_values[s[i-1]]
    print(value)

romanToInt('III') #3
romanToInt('IV') #4
romanToInt('IX') #9
romanToInt('LVIII') #58
