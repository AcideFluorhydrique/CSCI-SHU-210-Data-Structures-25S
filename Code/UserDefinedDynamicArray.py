"""
The UserDefinedDynamicArray class is a custom 
implementation of a dynamic array in Python, 
similar to Python's built-in list but with explicit 
control over underlying array storage and resizing logic. 
"""
import ctypes

class UserDefinedDynamicArray:
    def __init__(self, I = None):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        if I:
            self.extend(I)

    def __len__(self):
        return self._n

    def append(self, x):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = x
        self._n += 1

    def _resize(self, newsize):
        A = self._make_array(newsize)
        self._capacity = newsize
        for i in range(self._n):
            A[i] = self._A[i]
        self._A = A

    def _make_array(self, size):
        return (size * ctypes.py_object)()

    def __getitem__(self, i):
        if isinstance(i, slice):
            A = UserDefinedDynamicArray()
            for j in range(*i.indices(self._n)):
                A.append(self._A[j])
            return A
        if i < 0:
            i = self._n + i
        return self._A[i]

    def __delitem__(self, i):
        if isinstance(i, slice):
            for j in reversed(range(*i.indices(self._n))):
                del self[j]
        else:
            if i < 0:
                i = self._n + i
            for j in range(i, self._n - 1):
                self._A[j] = self._A[j + 1]
            self[-1] = None
            self._n -= 1

    def __str__(self):
        return "[" \
            + "".join(str(i) + "," for i in self[:-1]) \
            + (str(self[-1]) if not self.is_empty() else "") \
            + "]"

    def is_empty(self):
        return self._n == 0

    def __iter__(self):
        for i in range(self._n):
            yield self._A[i]

    def __setitem__(self, i, x):
        if i < 0:
            i += self._n
        self._A[i] = x

    def extend(self, I):
        iterable_len = len(I)
        if self._n + iterable_len > self._capacity:
            new_capacity = max(self._capacity * 2, self._n + iterable_len)
            self._resize(new_capacity)
        for index, value in enumerate(I):
            self._A[self._n + index] = value
        self._n += iterable_len

    def reverse(self):
        for i in range(len(self) // 2):
            j = len(self) - 1 - i
            self._A[i], self._A[j] = self._A[j], self._A[i]

    def __contains__(self, x):
        for each in self:
            if each == x:
                return True
        return False
