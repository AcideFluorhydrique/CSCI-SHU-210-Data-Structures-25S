from importlib.metadata import pass_none


class Empty(Exception):
    pass


class LinkQueue:
    __slots__ = "_head", "_tail", "_size"

    class _Node:
        __slots__ = "_element", "_next"

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
            raise Empty("Queue is empty")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, item):
        newest = self._Node(item, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


class Tree:
    class Position:

        def element(self):
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        return NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        raise NotImplementedError("must be implemented by subclass")

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def positions(self):
        return self.breadthfirst()

    def breadthfirst(self):
        if self.is_empty():
            raise Empty("tree is None")
        else:
            queue = LinkQueue()
            queue.enqueue(self.root())
            while len(queue) != 0:
                node = queue.dequeue()
                yield node
                for children in self.children(node):
                    queue.enqueue(children)


class BinaryTree(Tree):

    def left(self, p):
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        raise NotImplementedError("must be implemented by subclass")

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError("Root exists")
        self._size += 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child exists.")
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
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
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")
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

    def _delete_subtree(self, p):
        linkqueue = LinkQueue()
        linkqueue.enqueue(p)
        while len(linkqueue) != 0:
            node = linkqueue.dequeue()
            print(node.element(), end=' ')
            for children in self.children(node):
                linkqueue.enqueue(children)
            node._node._parent = node._node._left = node._node._right = node._node._element = None

    def _swap(self, e, q):
        # TODO: Please write your code here
        # Time complexity requirement: O(1)
        # Space complexity requirement: O(1)

        ## e 和 q 都是 Node
        # temp = e._node._element
        # e._node._element = q._node._element
        # q._node._element = temp

        # e._node._element, q._node._element =q._node._element, e._node._element

        # q._left = temp._left
        # q._right = temp._right

        node_e = self._validate(e)
        node_q = self._validate(q)
        parent_e = node_e._parent # 获取两个节点的父节点
        parent_q = node_q._parent


        if parent_e is node_q or parent_q is node_e:
            # TODO: 等会再想这个
            pass


        """两个节点共享一个父节点"""
        if parent_e is parent_q:
            if parent_e is not None:# 父节点存在时
                # 在父节点中交换两个子节点的位置
                if parent_e._left is node_e:
                    parent_e._left, parent_e._right = node_q, node_e
                else:
                    parent_e._right, parent_e._left = node_q, node_e
            # pass

        else:# 当两个节点有不同父节点时
            if parent_e is not None:
                if parent_e._left is node_e:
                    parent_e._left = node_q
                else:
                    parent_e._right = node_q
            else:  # node_p 根节点
                self._root = node_q

            if parent_q is not None:
                if parent_q._left is node_q:
                    parent_q._left = node_e
                else:
                    parent_q._right = node_e
            else:
                self._root = node_e
        node_e._parent, node_q._parent = node_q._parent, node_e._parent

        # 交换两个节点的子树结构
        node_e._left, node_q._left = node_q._left, node_e._left
        node_e._right, node_q._right = node_q._right, node_e._right

        # 更新父指针
        if node_e._left:
            node_e._left._parent = node_e
        if node_e._right:
            node_e._right._parent = node_e
        if node_q._left:
            node_q._left._parent = node_q
        if node_q._right:
            node_q._right._parent = node_q
        # pass


def main():
    tree = LinkedBinaryTree()
    root = tree._add_root("Providence")
    left = tree._add_left(root, "Chicago")
    right = tree._add_right(root, "Seattle")
    tree._add_left(left, "Baltimore")
    tree._add_right(left, "New York")

    id_root_old = id(tree.root()._node)
    print(id_root_old, tree.root().element())  # should print <memory id> "Providence"
    id_left_old = id(tree.left(tree.root())._node)
    tree._swap(root, left)  # swap root and left node
    id_root_new = id(tree.root()._node)
    id_left_new = id(tree.left(tree.root())._node)

    print(id_root_new, tree.root().element())  # should print <memory id> "Chicago"

    print(id_root_old == id_left_new and id_root_new == id_left_old)  # should print true


if __name__ == '__main__':
    main()
