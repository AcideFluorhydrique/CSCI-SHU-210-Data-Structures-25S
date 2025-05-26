"""
The ArrayDeque class implements a double-ended 
queue (deque) using a fixed-size circular array. 
A deque allows elements to be added and removed 
from both the front and the rear, making it a 
more versatile data structure than a simple queue.
"""

class ArrayDeque:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == len(self._data)

    def first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        loc = (self._front + self._size - 1) % len(self._data)
        return self._data[loc]

    def delete_first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        ans = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return ans

    def add_first(self, e):
        if self.is_full():
            raise Exception("Deque is full")
        loc = (self._front - 1) % len(self._data)
        self._data[loc] = e
        self._front = (self._front - 1) % len(self._data)
        self._size += 1

    def delete_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        loc = (self._front + self._size - 1) % len(self._data)
        ans = self._data[loc]
        self._data[loc] = None
        self._size -= 1
        return ans

    def add_last(self, e):
        if self.is_full():
            raise Exception("Deque is full")
        loc = (self._front + self._size) % len(self._data)
        self._data[loc] = e
        self._size += 1

    def __str__(self):
        return str(self._data)
