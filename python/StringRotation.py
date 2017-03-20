# code for exercise 1.9 - Assume you have a method isSubstring which checks if one word is a substring
#of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
#call to isSubstring (e.g., "waterbottle" is a rotation of" erbottlewat").
#
# Author: Iara Ribeiro - March/2017
#
# In this case, we gonna consider "in" as the java method isSubstring # 

def solution(s1, s2):
	rotation_word = s1+s1
	result = False

	if len(s2) == len(s1) and len(s1) > 0:
		result = s2 in rotation_word

	return result



def test(args1,args2,expect):
	print("Expect: " + str(expect) + ", was: " + str(solution(args1, args2)))

test("waterbottle","erbottlewat",True)
test("water","later",False)
test("","the",False)
