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


class BinaryTreeWithoutPosition:
    class TreeNode:
        def __init__(self, element, parent=None, left=None, right=None):
            self._parent = parent
            self._element = element
            self._left = left
            self._right = right
            self._height = 0

    def __init__(self):
        self._root = None
        self._size = 0

    # -------------------------- public accessors ---------------------------------

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

    # -------------------------- nonpublic mutators --------------------------

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


class BinarySearchTreeWithoutPosition(BinaryTreeWithoutPosition):

    # ------------------------------- nonpublic utilities -------------------------------

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

    # --------------------- public methods providing Binary Search Tree support ---------------------

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

        # --------------------- public methods for accessing/mutating ---------------------

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
            if v == node._element:  # If value already exists, don't insert
                return
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

    def _get_height(self, node):
        return node._height if node is not None else -1

    def left_rotate(self, pivot):
        # 获取将成为新子树根的右子节点
        r = pivot._right
        if r is None:  # 如果没有右子节点，无法旋转
            return;

        parent = pivot._parent
        t2 = r._left
        r._left = pivot
        pivot._right = t2
        r._parent = parent
        if parent is None:  # pivot 是根节点
            self._root = r
        elif parent._left == pivot:  # pivot 是左子节点
            parent._left = r
        else:  # pivot 是右子节点
            parent._right = r
        pivot._parent = r
        if t2 is not None:
            t2._parent = pivot
        # 自底向上更新高度
        pivot._height = 1 + max(
            self._get_height(pivot._left),
            self._get_height(pivot._right)
        )
        r._height = 1 + max(
            self._get_height(r._left),
            self._get_height(r._right)
        )

        # pass

    def right_rotate(self, pivot):
        # 获取将成为新子树根的左子节点
        l = pivot._left
        if l is None:  # 如果没有左子节点，无法旋转
            return;

        parent = pivot._parent
        t2 = l._right
        l._right = pivot
        pivot._left = t2
        l._parent = parent
        if parent is None:  # pivot 是根节点
            self._root = l
        elif parent._left == pivot:  # pivot 是左子节点
            parent._left = l
        else:  # pivot 是右子节点
            parent._right = l
        pivot._parent = l
        if t2 is not None:
            t2._parent = pivot
        # 自底向上更新高度
        pivot._height = 1 + max(
            self._get_height(pivot._left),
            self._get_height(pivot._right),
        )
        l._height = 1 + max(
            self._get_height(l._left),
            self._get_height(l._right),
        )
        # pass

    def left_right_rotate(self, node):
        # 执行左-右双旋转：
        # 1. 对左子节点进行左旋转
        # 2. 对当前节点进行右旋转
        if node._left is None:
            return
        self.left_rotate(node._left)
        self.right_rotate(node)
        # pass

    def right_left_rotate(self, node):
        # 执行右-左双旋转：
        # 1. 对右子节点进行右旋转
        # 2. 对当前节点进行左旋转
        if node._right is None:
            return
        self.right_rotate(node._right)
        self.left_rotate(node)
        # pass

    def _rebalance_insert(self, node):
        while node is not None:
            # 更新当前节点的高度
            node._height = 1 + max(
                self._get_height(node._left),
                self._get_height(node._right)
            )
            # 计算平衡因子
            balance = self._get_height(node._left) - self._get_height(node._right)
            # 情况1：左重
            if balance > 1:
                if self._get_height(node._left._left) >= self._get_height(node._left._right):
                    # 左-左情况：单次右旋转
                    self.right_rotate(node)
                else:
                    # 左-右情况：双旋转
                    # 先对左子节点左旋转
                    self.left_rotate(node._left)
                    # 再对当前节点右旋转
                    self.right_rotate(node)
                break
            # 情况2：右重
            elif balance < -1:
                if self._get_height(node._right._right) >= self._get_height(node._right._left):
                    # 右-右情况：单次左旋转
                    self.left_rotate(node)
                else:
                    # 右-左情况：双旋转
                    # 先对右子节点右旋转
                    self.right_rotate(node._right)
                    # 再对当前节点左旋转
                    self.left_rotate(node)
                break
            # 向上移动到父节点
            node = node._parent
        # pass


    def _rebalance_delete(self, p):
        # You don't need to implement this method.
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


def main():
    bst_ll = BinarySearchTreeWithoutPosition()
    root = bst_ll.add_root(3)
    node2 = bst_ll.add_left(root, 2)
    leaf1 = bst_ll.add_left(node2, 1)
    bst_ll.right_rotate(root)
    inorder_ll = list(bst_ll)
    assert inorder_ll == [1, 2, 3], f"LL-inorder should be [1,2,3], got {inorder_ll}"
    preorder_ll = [n._element for n in bst_ll.preorder()]
    assert preorder_ll == [2, 1, 3], f"LL-preorder should be [2,1,3], got {preorder_ll}"

    bst_rr = BinarySearchTreeWithoutPosition()
    root2 = bst_rr.add_root(1)
    node2b = bst_rr.add_right(root2, 2)
    leaf3 = bst_rr.add_right(node2b, 3)
    bst_rr.left_rotate(root2)
    inorder_rr = list(bst_rr)
    assert inorder_rr == [1, 2, 3], f"RR-inorder should be [1,2,3], got {inorder_rr}"
    preorder_rr = [n._element for n in bst_rr.preorder()]
    assert preorder_rr == [2, 1, 3], f"RR-preorder should be [2,1,3], got {preorder_rr}"

    bst_lr = BinarySearchTreeWithoutPosition()
    root3 = bst_lr.add_root(3)
    node1 = bst_lr.add_left(root3, 1)
    node2 = bst_lr.add_right(node1, 2)
    bst_lr.left_right_rotate(root3)
    inorder_lr = list(bst_lr)
    assert inorder_lr == [1, 2, 3], f"LR-inorder should be [1,2,3], got {inorder_lr}"
    preorder_lr = [n._element for n in bst_lr.preorder()]
    assert preorder_lr == [2, 1, 3], f"LR-preorder should be [2,1,3], got {preorder_lr}"

    bst_rl = BinarySearchTreeWithoutPosition()
    root4 = bst_rl.add_root(1)
    node3 = bst_rl.add_right(root4, 3)
    node2b = bst_rl.add_left(node3, 2)
    bst_rl.right_left_rotate(root4)
    inorder_rl = list(bst_rl)
    assert inorder_rl == [1, 2, 3], f"RL-inorder should be [1,2,3], got {inorder_rl}"
    preorder_rl = [n._element for n in bst_rl.preorder()]
    assert preorder_rl == [2, 1, 3], f"RL-preorder should be [2,1,3], got {preorder_rl}"

    bst_all = BinarySearchTreeWithoutPosition()
    for v in range(1, 8):
        bst_all.insert(v)
    inorder_all = list(bst_all)
    assert inorder_all == [1, 2, 3, 4, 5, 6, 7], f"In-order should be [1..7], got {inorder_all}"
    preorder_all = [n._element for n in bst_all.preorder()]
    expected_pre_all = [4, 2, 1, 3, 6, 5, 7]
    assert preorder_all == expected_pre_all, (
        f"AVL-preorder should be {expected_pre_all}, got {preorder_all}"
    )

    print("All rotation tests (LL, RR, LR, RL) and AVL insertion passed.")


if __name__ == '__main__':
    main()
