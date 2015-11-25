class LinkedList:
	def __init__(self):
		self.car = None
		self.cdr = None

	def __repr__(self):
		if self.cdr is None:
			return str(self.car)
		else:
			return str(self.car) + ' -> ' + str(self.cdr)

class HashMap:
	def __init__(self, hash_function = lambda x: x % 10, size = 10):
		self.hash_map = [ None for i in range(size) ]
		self.hash_function = hash_function

	def put(self, key, value):
		index = self.hash_function(key)
		prev_elem = None
		curr_elem = self.hash_map[index]
		while curr_elem is not None:
			if curr_elem.car[0] == key:
				curr_elem.car[1] = value
				return

			prev_elem = curr_elem
			curr_elem = curr_elem.cdr

		new_elem = LinkedList()
		new_elem.car = [key, value]

		if prev_elem is None:	
			self.hash_map[index] = new_elem
		else:
			prev_elem.cdr = new_elem

	def get(self, key):
		index = self.hash_function(key)
		curr_elem = self.hash_map[index]
		while curr_elem is not None:
			if curr_elem.car[0] == key:
				return curr_elem.car[1]

			curr_elem = curr_elem.cdr

		return None

	def remove(self, key):
		index = self.hash_function(key)
		prev_elem = None
		curr_elem = self.hash_map[index]
		while curr_elem is not None:
			if curr_elem.car[0] == key:
				if prev_elem is None:
					self.hash_map[index] = curr_elem.cdr
				else:
					prev_elem.cdr = curr_elem.cdr

				return

			prev_elem = curr_elem
			curr_elem = curr_elem.cdr

	def __repr__(self):
		r = []
		for i in self.hash_map:
			if i is not None:
				r.append(str(i))
			else:
				r.append('')
		return '\n'.join(r)