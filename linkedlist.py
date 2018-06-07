# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
print("Linked List in Python")
class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self,newdata):
		self.data = newdata
	def setNext(self,newnext):
		self.next = newnext

class UnorderedList:
	def __init__(self):
		self.head = None
	def isEmpty(self):
		return self.head == None
	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count
	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found
	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
	def showlist(self):
		pos = self.head
		if pos != None:
			cnt = 0
			content = []
			while pos != None:
				content.append(pos.getData())
				pos = pos.getNext()
				cnt = cnt + 1
			print("Content of list: " + str(content))
		else:
			print("No content in list")

print('Begin UnorderedList pipe')
mylist = UnorderedList()
mylist.showlist()
mylist.add(31)
mylist.showlist()
mylist.add(77)
mylist.showlist()
mylist.add(17)
mylist.showlist()
mylist.add(93)
mylist.showlist()
mylist.add(26)
mylist.showlist()
mylist.add(54)
mylist.showlist()

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))

print("")
print("Ordered List")

class OrderedList:
	def __init__(self):
		self.head = None
	def search(self,item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()
		return found
	def add(self,item):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()
		temp = Node(item)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current)
			previous.setNext(temp)
	def isEmpty(self):
		return self.head == None
	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count
	def showlist(self):
		pos = self.head
		if pos != None:
			cnt = 0
			content = []
			while pos != None:
				content.append(pos.getData())
				pos = pos.getNext()
				cnt = cnt + 1
			print("Content of list: " + str(content))
		else:
			print("No content in list")

print('Begin OrderedList')
mylist = OrderedList()
mylist.showlist()
mylist.add(31)
mylist.showlist()
mylist.add(77)
mylist.showlist()
mylist.add(17)
mylist.showlist()
mylist.add(93)
mylist.showlist()
mylist.add(26)
mylist.showlist()
mylist.add(54)
mylist.showlist()

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
