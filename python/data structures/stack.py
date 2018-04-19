class Stack:
	"""
	Class that implements a stack in python

	Methods
	-------

	pop()
		Remove the top item from the stack
	push(item)
		Add an item to the top of the stack
	peek()
		Return the top of the stack
	is_empty()
		Return true if and only if the stack is empty
	"""

	def __init__(self):
		self.stack = []

	def pop(self):
		"""
		Remove the top item from the stack

		Raises
		------
		ValueError
			If the stack is empty.
		"""
		if self.is_empty():
			raise ValueError('The stack is empty')
		else:
			item = self.stack[0]
			del self.stack[0]
			return item

	def push(self, value):
		"""
		Add an item to the top of the stack

		Attributes
		----------
		value
			The element to be added in the top of the stack
		"""
		self.stack.insert(0,value)

	def peek(self):
		"""
		Return the top of the stack

		Return
		------

		The element in the top of the stack
		"""
		return self.stack[0]

	def is_empty(self):
		"""
		Return true if and only if the stack is empty

		Return
		------
		Boolean
			True the list is empty and false if is not.
		"""
		if len(self.stack) == 0:
			return True
		else:
			return False

