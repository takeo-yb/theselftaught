class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		# return self.items == []
		return not self.items

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		last = len(self.items) - 1
		return self.items[last]
		# return self.items[-1]

	def size(self):
		return len(self.items)

stack = Stack()
stack.push(1)
item = stack.pop()
print(item)
print(stack.is_empty())

for i in range(0, 6):
        stack.push(i)
 
print(stack.peek())
print(stack.size())

while stack.size():
        stack.pop()

for c in "Hello":
        stack.push(c)

reverse = ""

while stack.size():
        reverse += stack.pop()

print(reverse)

while stack.size():
        stack.pop()

for c in "yesterday":
        stack.push(c)

reversed_string = ""

while stack.size():
        reversed_string += stack.pop()

print(reversed_string)

while stack.size():
        stack.pop()

list1 = [1,2,3,4,5]
list2 = []

for i in list1:
        stack.push(i)

for i in range(stack.size()):
        list2.append(stack.pop())

print(list1)
print(list2)
