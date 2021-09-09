def shiftingLetters(s, shifts):
    s = list(s)

    prev = 0
    for i in range(len(shifts) - 1, -1, -1):
        shifts[i] = (shifts[i] + prev) % 26
        prev = shifts[i]
        new_val = ord(s[i]) + shifts[i]
        
        if new_val > 122:
            new_val = new_val - 122 - 1 + 97
                
        s[i] = chr(new_val)
        
    print(''.join(s))


shiftingLetters("bad",[10,20,30])
shiftingLetters("aaa", [1,2,3])
