# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaDequeinPython.html
print("Deque in Python")

class Deque:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.append(item)
		print("added to front: " + str(item))

	def addRear(self, item):
		self.items.insert(0,item)
		print("added to rear: " + str(item))

	def removeFront(self):
		var = self.items.pop()
		print("remove from front: " + str(var))
		return var

	def removeRear(self):
		var = self.items.pop(0)
		print("remove from rear: " + str(var))
		return var

	def size(self):
		return len(self.items)

d=Deque()
print("Deque is empty ? ")
print(d.isEmpty())
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print("What is size of Deque ? " + str(d.size()))
print("Deque is empty ?")
print(d.isEmpty())
d.addRear(8.4)
print(d.removeRear())
print(d.removeFront())

print('')
print("Panlindrome Checker using Deque in Python")
from pythonds.basic.deque import Deque

def palchecker(aString):
	chardeque = Deque()

	for ch in aString:
		chardeque.addRear(ch)

	stillEqual = True

	while chardeque.size() > 1 and stillEqual:
		first = chardeque.removeFront()
		last = chardeque.removeRear()
		if first != last:
			stillEqual = False

	return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
print(palchecker("madam"))
