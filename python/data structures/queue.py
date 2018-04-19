class Queue:
	"""
	Class that implements a queue in python

	Methods
	-------

	remove()
		Remove the bottom item from the queue
	add(value)
		Add an item to the end of the queue
	peek()
		Return the bottom of the queue
	is_empty()
		Return true if and only if the queue is empty
	"""

	def __init__(self):
		self.queue = []

	def remove(self):
		"""
		Remove the bottom item from the queue

		Raises
		------
		ValueError
			If the queue is empty.
		"""
		if self.is_empty():
			raise ValueError('The queue is empty')
		else:
			item = self.queue[-1]
			del self.queue[-1]
			return item

	def add(self, value):
		"""
		Add an item to the end of the queue

		Attributes
		----------
		value
			The element to be added in the top of the queue
		"""
		self.queue.insert(0,value)

	def peek(self):
		"""
		Return the bottom of the queue

		Return
		------

		The element in the bottom of the queue
		"""
		return self.queue[-1]

	def is_empty(self):
		"""
		Return true if and only if the queue is empty

		Return
		------
		Boolean
			True the queue is empty and false if is not.
		"""
		if len(self.queue) == 0:
			return True
		else:
			return False

