class TreeWithParent:
  def __init__(self, element, parent = None, left = None, right = None):
    self._element = element
    self._parent = parent
    self._left = left
    self._right = right

  def __str__(self):
  	return str(self._element)
