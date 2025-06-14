# The BinaryTreeWithoutPosition class models a simple binary tree structure, where each node of the tree can have up to two children (left and right), a parent, and contains an element. 

class BinaryTreeWithoutPosition:
    class TreeNode:
        def __init__(self, element, parent = None, left = None, right = None):
            self._parent = parent
            self._element = element
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

    #-------------------------- public accessors ---------------------------------
  
    def __len__(self):
        return self._size

    def is_root(self, node):
        return self._root == node

    def is_leaf(self, node):
        return self.num_children(node) == 0

    def is_empty(self):
        return len(self) == 0

    def __iter__(self):
        for node in self.nodes():                       
            yield node._element                               

    def depth(self, node):
        if self.is_root(node):
            return 0
        else:
            return 1 + self.depth(self.parent(node))

    def _height1(self):                
        return max(self.depth(node) for node in self.nodes() if self.is_leaf(node))

    def _height2(self, node):                  
        if self.is_leaf(node):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(node))

    def height(self, node=None):
        if node is None:
            node = self._root
        return self._height2(node)        

    def nodes(self):
        return self.preorder()                          

    def preorder(self):
        if not self.is_empty():
            for node in self._subtree_preorder(self._root):
                yield node

    def _subtree_preorder(self, node):
        yield node                                          
        for c in self.children(node):                       
            for other in self._subtree_preorder(c):        
                yield other                                

    def postorder(self):
        if not self.is_empty():
            for node in self._subtree_postorder(self._root):
                yield node

    def _subtree_postorder(self, node):
        for c in self.children(node):                        
            for other in self._subtree_postorder(c):       
                yield other                                
        yield node                                         
    def inorder(self):
        if not self.is_empty():
          for node in self._subtree_inorder(self._root):
            yield node

    def _subtree_inorder(self, node):
        if node._left is not None:          
          for other in self._subtree_inorder(node._left):
            yield other
        yield node                              
        if node._right is not None:         
          for other in self._subtree_inorder(node._right):
            yield other

    def breadthfirst(self):
        if not self.is_empty():
            fringe = LinkedQueue()            
            fringe.enqueue(self._root)       
            while not fringe.is_empty():
                node = fringe.dequeue()             
                yield node                         
                for c in self.children(node):
                    fringe.enqueue(c)             

    def root(self):
        return self._root

    def parent(self, node):
        return node._parent

    def left(self, node):
        return node._left

    def right(self, node):
        return node._right

    def children(self, node):
        if node._left is not None:
            yield node._left
        if node._right is not None:
            yield node._right

    def num_children(self, node):
        count = 0
        if node._left is not None:    
            count += 1
        if node._right is not None: 
            count += 1
        return count

    def sibling(self, node):
        parent = node._parent
        if parent is None:                  
            return None                        
        else:
            if node == parent._left:
                return parent._right   
            else:
                return parent._left

    #-------------------------- nonpublic mutators --------------------------

    def add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self.TreeNode(e)
        return self._root

    def add_left(self, node, e):
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self.TreeNode(e, node)           
        return node._left

    def add_right(self, node, e):
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self.TreeNode(e, node)        
        return node._right

    def _replace(self, node, e):
        old = node._element
        node._element = e
        return old

    def _delete(self, node):
        if self.num_children(node) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent   
        if node is self._root:
            self._root = child       
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        return node._element

    def _attach(self, node, t1, t2):
        if not self.is_leaf(node):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):    
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():        
            t1._root._parent = node
            node._left = t1._root
            t1._root = None            
            t1._size = 0
        if not t2.is_empty():       
            t2._root._parent = node
            node._right = t2._root
            t2._root = None          
            t2._size = 0
