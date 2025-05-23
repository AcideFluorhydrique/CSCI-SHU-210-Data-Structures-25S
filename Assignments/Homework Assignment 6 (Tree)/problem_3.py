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

        def __str__(self):
            return str(self._element)

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

    def preorderPrint(self, node):
        if node is None:
            return
        for each in self._subtree_preorder(node):
            print(each._element, end=" ")

    def postorderPrint(self, node):
        if node is None:
            return
        for each in self._subtree_postorder(node):
            print(each._element, end=" ")

    def inorderPrint(self, node):
        if node is None:
            return
        for each in self._subtree_inorder(node):
            print(each._element, end=" ")

    def levelorderPrint(self, node):
        queue = LinkedQueue()
        queue.enqueue(node)
        while not queue.is_empty():
            next_node = queue.dequeue()
            print(next_node._element, end=" ")
            if next_node._left:
                queue.enqueue(next_node._left)
            if next_node._right:
                queue.enqueue(next_node._right)

    def height(self, node=None):
        if node is None:
            node = self._root
        if self.is_leaf(node):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(node))

    def depth(self, node):
        if self.is_root(node):
            return 0
        else:
            return 1 + self.depth(node._parent)

    def return_max(self):
        maximum = self._root._element
        for each in self:
            if each > maximum:
                maximum = each
        return maximum

    def flip_node(self, node):
        node._left, node._right = node._right, node._left

    def flip_tree(self, node=None):
        if node is None:
            node = self._root
        node._left, node._right = node._right, node._left
        if node._left:
            self.flip_tree(node._left)
        if node._right:
            self.flip_tree(node._right)

    def is_isomorphic(self, other):
        # TODO: Please write your code here

        def helpf(node1, node2):

            if node1 is None and node2 is None:
                return True

            elif node1 is None or node2 is None:
                return False

            if node1._element != node2._element:
                return False

            num_children1 = self.num_children(node1)
            num_children2 = other.num_children(node2)
            if num_children1 != num_children2:
                return False # 子 的数量必须一样



            # Both leaves
            if num_children1 == 0:
                return True

            # Both one
            elif num_children1 == 1:
                child1 = node1._left if node1._left is not None else node1._right
                child2 = node2._left if node2._left is not None else node2._right
                return helpf(child1, child2)

            # Both two children
            else:
                left1, right1 = node1._left, node1._right
                left2, right2 = node2._left, node2._right
                return (helpf(left1, left2) and helpf(right1, right2)) or \
                    (helpf(left1, right2) and helpf(right1, left2)
                )

        return helpf(self._root, other._root)

        # pass


def main():
    t1 = Tree()
    a = t1.add_root(1)
    b = t1.add_left(a, 3)
    c = t1.add_right(a, 2)
    d = t1.add_left(b, 4)

    t2 = Tree()
    a = t2.add_root(1)
    b = t2.add_left(a, 3)
    c = t2.add_right(a, 2)
    d = t2.add_left(b, 4)

    t2.flip_node(a)

    print(t1.is_isomorphic(t2))  # should print True


if __name__ == '__main__':
    main()
