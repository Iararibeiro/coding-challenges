""" 
This algorithm implements a generic version of a Stack in python, the idea
with the algorithm in this directory is have a source for future reference in
problems from codility or similar sites/problems.

The algorithm used the theory presented in Introduction to Algorithms, 
a book by Thomas H. Cormen.

@author: Iara Ribeiro - 11/12/2016.
""" 
class Stack():
	
	def __init__(self):
		self.top = 0
		self.S = []

	def stackEmpty(self):
		if(self.top == 0):
			return "true"
		return "false"
	
	def push(self,x):
		self.top= self.top + 1
		self.S.insert(self.top, x)

	def pop(self):
		if(self.top == 0):
			return "underflow"
		else:
			self.S.remove(self.S[(self.top-1)])
			self.top = self.top - 1
	
	def print_stack(self):
		result = "[";
		for i in range(0,self.top):
			if(i==0):
				result += self.S[i]
			else:
				result = result + "," + self.S[i]
		return result+"]"

	def test(functionToTest, args, expected):
		result = functionToTest(args)
		print "Expected " + expected + ", was " + result		

if __name__ == '__main__':
    s = Stack()
    print("Expected " + s.stackEmpty() + ", was " + "true")
    s.push("banana")
    print("Expected " +"[banana]" + ", was " + s.print_stack())
    s.push("apple")
    print("Expected " +"[banana,apple]"+ ", was " +s.print_stack())
    s.pop()
    print("Expected " +"[banana]" + ", was " + s.print_stack())    
    s.push("pineapple")
    print("Expected " +"[banana,pineapple]"+ ", was " +s.print_stack())
    s.pop()
    s.pop()
    print("Expected " +"[]"+ ", was " +s.print_stack())