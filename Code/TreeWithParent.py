"""
The TreeWithParent class is a simple representation of a node in a binary tree where 
each node contains an element and may have parent, left, and right child nodes. 
The class keeps a reference to a parent node, hence the name TreeWithParent.
"""

class TreeWithParent:
  def __init__(self, element, parent = None, left = None, right = None):
    self._element = element
    self._parent = parent
    self._left = left
    self._right = right

  def __str__(self):
  	return str(self._element)
