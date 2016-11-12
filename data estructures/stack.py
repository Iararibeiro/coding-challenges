""" 
This algorithm implements a generic version of a Stack in javascript, the idea
with the algorithm in this directory is have a source for future reference in
problems from codility or similar sites/problems.

The algorithm used the theory presented in Introduction to Algorithms, 
a book by Thomas H. Cormen.

@author: Iara Ribeiro - 11/12/2016.
""" 

top = 0;
S = [];

def stackEmpty(S):
	if(top == 0):
		return "true"
	return "false"

def push(S,x):
	top += 1
	S[top] = x


"""
function pop(S){
	if(stackEmpty(S)){
		return "stack empty";
	}else{
		top -= 1;
		return S[top + 1];
	}
}
"""

def print_stack(S):
	result = "[";
	for i in range(1,top):
		if( i ==1):
			result += S[i];
		else:
			result = result + "," + S[i];
	return result+"]";


def test(functionToTest, args, expected):
	result = functionToTest(args)
	print "Expected " + expected + ", was " + result

test(stackEmpty, S, "true");
push(S,"banana");
test(print_stack, [S], "[banana]");
#push(S,"apple");
#test(print, [S], "[banana,apple]");
#pop(S);
#test(print, [S], "[banana]");
#push(S,"pineapple");
#test(print, [S], "[banana,pineapple]");
#pop(S);
#test(print, [S], "[]");