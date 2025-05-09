"""
The ArrayStack class implements a stack data structure using a Python list. 
The stack is a linear data structure that follows 
the Last In, First Out (LIFO) principle, where elements 
are added and removed from the same end.
"""

class ArrayStack:
  def __init__(self):
  	self.array = []
  
  def __len__(self):
  	return len(self.array)

  def is_empty(self):
  	return len(self.array) == 0

  def push(self, e):
  	self.array.append(e)

  def top(self):
  	if self.is_empty():
  		raise Exception()
  	return self.array[-1]

  def pop(self):
  	if self.is_empty():
  		raise Exception()
  	return self.array.pop(-1)

  def __repr__(self):
  	return str(self.array)