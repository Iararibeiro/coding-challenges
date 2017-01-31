class Item:

	key = 0
	value = ""

	def __init__(self, key, value):
		self.key = key
		self.value = value

	def print_item(self):
		return "key:"+str(self.key)+" , value: " + self.value

class HashTable:
	size = 0
	hash_table = []

	def __init__(self, size):
		self.size = size
		self.hash_table = [[] for i in range(size)]


	def hashing(self,key):
		hashing = key % self.size
		return hashing

	def hash_insert(self, item):
		hashing = self.hashing(item.key)
		self.hash_table[hashing].append(item)

	def search(self, key):
		hashing = self.hashing(key)

		if self.hash_table[hashing] == []:
			return False
		else:
			slot = self.hash_table[hashing]
			for item in range(0,len(slot)):
				if slot[item].key == key:
					print slot[item].print_item()
					return slot[item]
			return False

	def remove(self, key, value):
		hashing = self.hashing(key)

		if self.hash_table[hashing] == []:
			return False
		else:
			slot = self.hash_table[hashing]
			for item in range(0,len(slot)):
				if slot[item].key == key and slot[item].value == value:
					slot.remove(slot[item])
					return True
			return False

if __name__ == "__main__":
	ht = HashTable(100)
	i1 = Item(20,"v1")
	i2 = Item(17,"v2")

	print ht.hashing(i1.key)
	print ht.hash_insert(i1)
	print ht.hash_insert(i2)
	ht.search(20)
	ht.remove(20,"v1")
	print ht.search(2)