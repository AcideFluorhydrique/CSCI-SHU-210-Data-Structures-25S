class Empty(Exception):
    pass


class Error(Exception):
    pass


class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def __str__(self):
        result = []
        curNode = self._head
        while curNode is not None:
            result.append(str(curNode._element) + " --> ")
            curNode = curNode._next
        result.append("None")
        return "".join(result)


class Tree:
    class TreeNode:
        def __init__(self, element, parent=None, left=None, right=None):
            self._parent = parent
            self._element = element
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

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


class BinarySearchTree(Tree):

    def _subtree_search(self, node, v):
        if v == node._element:
            return node
        elif v < node._element:
            if node._left is not None:
                return self._subtree_search(node._left, v)
        else:
            if node._right is not None:
                return self._subtree_search(node._right, v)
        return node

    def _subtree_first_position(self, node):
        walk = node
        while walk._left is not None:
            walk = walk._left
        return walk

    def _subtree_last_position(self, node):
        walk = node
        while walk._right is not None:
            walk = walk._right
        return walk

    def first(self):
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, node):
        if node._left is not None:
            return self._subtree_last_position(node._left)
        else:
            walk = node
            above = walk._parent
            while above is not None and above._element > walk._element:
                walk = above
                above = walk._parent
            return above

    def after(self, node):
        if node._right is not None:
            return self._subtree_first_position(node._right)
        else:
            walk = node
            above = walk._parent
            while above is not None and above._element < walk._element:
                walk = above
                above = walk._parent
            return above

    def delete(self, node):
        if node._left and node._right:
            replacement = self._subtree_last_position(node._left)
            self._replace(node, replacement._element)
            node = replacement
        parent = node._parent
        self._delete(node)
        self._rebalance_delete(parent)

    def get_node(self, v):
        if self.is_empty():
            raise Empty('Tree is empty')
        else:
            node = self._subtree_search(self._root, v)
            if v != node._element:
                raise Error('Not found: ' + repr(v))
            return node

    def insert(self, v):
        if self.is_empty():
            leaf = self.add_root(v)
        else:
            node = self._subtree_search(self._root, v)
            if node._element < v:
                leaf = self.add_right(node, v)
            else:
                leaf = self.add_left(node, v)
        self._rebalance_insert(leaf)

    def delete_value(self, v):
        if not self.is_empty():
            node = self._subtree_search(self._root, v)
            if v == node._element:
                self.delete(node)
                return
        raise Error('Not found: ' + repr(v))

    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def __iter__(self):
        node = self.first()
        while node is not None:
            yield node._element
            node = self.after(node)

    def __reversed__(self):
        node = self.last()
        while node is not None:
            yield node._element
            node = self.before(node)

    def diameter(self):
        # TODO: Please write your code here
        _max = 0

        def helper(node):
            nonlocal _max


            if self.is_leaf(node):
                return 0;
            
            else:

                if node._left is not None:
                    lh = helper(node._left)
                else:
                    lh = -1

                if node._right is not None:
                    rh = helper(node._right)
                else:
                    rh = -1

                if lh >= 0 and rh >= 0:
                    c = lh + rh + 2
                elif lh >= 0:
                    c = lh + 1
                elif rh >= 0:
                    c = rh + 1
                else:
                    c = 0

                _max = max(_max, c)


                if lh >= 0 or rh >= 0:
                    return max(lh, rh) + 1;
                else:
                    return 0;
 

        helper(self._root)
        return _max
        pass


def main():
    bst = BinarySearchTree()
    bst.insert(18)
    bst.insert(6)
    bst.insert(21)
    bst.insert(24)
    bst.insert(1)
    bst.insert(9)
    bst.insert(0)
    bst.insert(4)
    bst.insert(10)
    bst.insert(14)
    bst.insert(12)
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)

    print(bst.diameter() == 8)  # should print True


if __name__ == '__main__':
    main()
