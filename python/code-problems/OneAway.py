def solution(word_one,word_two):
	size_one = len(word_one)
	size_two = len(word_two)
	if size_one < size_two:
		#insert
	    if size_two - size_one == 1:
			return replace(word_one[0:size_two],word_two)
	elif size_one > size_two:
		#delete
		return delete(word_one,word_two)
	else:
		return replace(word_one,word_two)

def delete(w1,w2):
	letters_one = 0
	letters_two = 0
	deleted = 0

	while letters_one != len(w1) and letters_two != len(w2):

		if w1[letters_one] == w2[letters_two]:
			letters_one += 1
			letters_two += 1
		elif w1[letters_one] != w2[letters_two]:
			letters_one += 1
			deleted += 1

	if deleted > 1:
		return False
	return True


def replace(w1,w2):
	replacement = 0

	for i in range(0, len(w1)):
		if w1[i] != w2[i]:
			replacement += 1
			if replacement > 1:
				return False
	return True 
	
def test(args1,args2, expect):
	print("Expect: " + str(expect) + ", was: " + str(solution(args1,args2)))

test("pale","ple",True)
test("pale","pales",True)
test("pales","pale",True)
test("pale","bale",True)
test("pale","bake",False)