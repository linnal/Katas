from  Node import * 

class LinkedQueue():

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def enqueue(self, elem):
		next_node = Node(elem, None)
		if self.size == 0:
			self.head = next_node
			self.tail = next_node
		else:
			self.tail.next = next_node
			self.tail = next_node

		self.size += 1

	def dequeue(self):
		deq_node = self.head
		self.head = self.head.next
		self.size -= 1
		return deq_node

	def to_string(self):
		res = ""
		node = self.head
		while node != None:
			res += "{} ".format(node.value)
			node = node.next
		return res

