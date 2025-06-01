"""
The TreeWithoutParent class is a simple representation of a node in a binary tree where each node contains an element and may have left and right child nodes. The class does not keep a reference to a parent node, hence the name TreeWithoutParent.
"""



class TreeWithoutParent:
    def __init__(self, element, left = None, right = None):
        self._element = element
        self._left = left
        self._right = right

    def __str__(self):
        return str(self._element)
