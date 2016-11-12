""" 
This algorithm implements a generic version of a Queue in python, the idea
with the algorithm in this directory is have a source for future reference in
problems from codility or similar sites/problems.

The algorithm used the theory presented in Introduction to Algorithms, 
a book by Thomas H. Cormen.

@author: Iara Ribeiro - 11/12/2016.
""" 
class Queue():
	
	def __init__(self):
		self.head = 0
		self.tail = 0
		self.Q = []

	def queue_empty(self):
		if self.tail == 0 :
			return "true"
		return "false"
	
	def enqueue(self,x):
		self.Q.insert(self.tail, x)
		self.tail = self.tail + 1

	def dequeue(self):
		self.head = self.head + 1

	def print_stack(self):
		result = "[";
		for i in range(self.head,self.tail):
			if (self.tail - i) == 1:
				result = result + self.Q[i];
			else:
				result = result + self.Q[i] + ",";
		return result+"]"

	def test(functionToTest, args, expected):
		result = functionToTest(args)
		print "Expected " + expected + ", was " + result		

if __name__ == '__main__':
    q = Queue()
    print("Expected " + q.queue_empty() + ", was " + "true")
    q.enqueue("banana")
    print("Expected " +"[banana]" + ", was " + q.print_stack())
    q.enqueue("apple")
    print("Expected " +"[banana,apple]"+ ", was " +q.print_stack())
    q.dequeue()
    print("Expected " +"[apple]" + ", was " + q.print_stack())    
    q.enqueue("pineapple")
    print("Expected " +"[apple,pineapple]"+ ", was " +q.print_stack())
    q.dequeue()
    q.dequeue()
    print("Expected " +"[]"+ ", was " +q.print_stack())