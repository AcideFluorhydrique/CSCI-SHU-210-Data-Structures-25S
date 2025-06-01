"""

"""



class TreeWithoutParent:
    def __init__(self, element, left = None, right = None):
        self._element = element
        self._left = left
        self._right = right

    def __str__(self):
        return str(self._element)
