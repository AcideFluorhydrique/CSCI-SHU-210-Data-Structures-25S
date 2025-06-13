class TwoFourTreeNode:
    def __init__(self):
        self.keys = [None] * 3  # A 2-4 tree can have 1-3 keys per node
        self.children = [None] * 4  # Maximum of 4 children
        self.parent = None

    def child_index(self, node):
        for idx, child in enumerate(self.children):
            if child is node:
                return idx
        return -1

    def is_leaf(self):
        return all(child is None for child in self.children)

    def __repr__(self):
        return f"<TwoFourTreeNode keys={self.keys}>"

    def search(self, key):
        count = 0
        while count < 3 and self.keys[count] is not None:
            count += 1

        for i in range(count):
            if key == self.keys[i]:
                return self, i
            if key < self.keys[i]:
                if self.is_leaf():
                    return None, -1
                return self.children[i].search(key)

        if self.is_leaf():
            return None, -1
        return self.children[count].search(key)

    def delete(self, key):
        """删除指定键，并保持2-4树平衡，返回新的根节点"""
        node, idx = self.search(key)
        if not node:
            return self

        # 如果不是叶子节点，用后继节点替换
        if not node.is_leaf():
            succ = node.children[idx + 1]
            while not succ.is_leaf():
                succ = succ.children[0]
            node.keys[idx] = succ.keys[0]

            return succ._delete_from_leaf(succ.keys[0])

        return node._delete_from_leaf(key)
        pass

    def _delete_from_leaf(self, key):
        """从叶子节点删除指定键，处理可能的下溢"""
        idx = -1
        for i in range(3):
            if self.keys[i] == key:
                idx = i
                break

        if idx == -1:
            return self

        # 删除键后左移
        for i in range(idx, 2):
            self.keys[i] = self.keys[i + 1]
        self.keys[2] = None

        # 如果是根节点直接返回
        if self.parent is None:
            return self

        # 如果还有键则无需调整
        if any(
            k is not None for k in self.keys
        ):
            return self.get_root()

        # 否则发生下溢
        return self._handle_underflow()

    def _handle_underflow(self):
        """处理节点为空的情况（下溢），尝试借键或合并兄弟节点"""
        p = self.parent
        pos = p.child_index(self)

        # 尝试向左兄弟借键
        if pos > 0:
            l = p.children[pos - 1]
            if sum(k is not None for k in l.keys) > 1:
                return self._borrow_from_left(l, p, pos)

        # 尝试向右兄弟借键
        if (pos < 3 and
            p.children[pos + 1]
        ):
            r = p.children[pos + 1]
            if sum(k is not None for k in r.keys) > 1:
                return self._borrow_from_right(r, p, pos)

        # 否则合并
        if pos > 0:
            return self._merge_with_left(
                p.children[pos - 1], p, pos
            )
        return self._merge_with_right(p.children[pos + 1], p, pos)
        pass

    def _borrow_from_left(self, l, p, pos):
        """从左兄弟节点借一个键"""
        self.keys[0] = p.keys[pos - 1]

        # 找到左兄弟中最大键的位置
        last = 0
        while (last < 2 and
               l.keys[last + 1] is not None
        ):
            last += 1

        p.keys[pos - 1] = l.keys[last]
        l.keys[last] = None

        if not self.is_leaf():
            for i in range(3, 0, -1):
                self.children[i] = self.children[i - 1]
            self.children[0] = l.children[last + 1]
            l.children[last + 1] = None
            if self.children[0]:
                self.children[0].parent = self

        return self.get_root(

        )
        pass

    def _borrow_from_right(self, r, p, pos):
        """从右兄弟节点借一个键"""
        self.keys[0] = p.keys[pos]
        p.keys[pos] = r.keys[0]

        for i in range(2):
            r.keys[i] = r.keys[i + 1]
        r.keys[2] = None

        if not self.is_leaf():
            self.children[1] = r.children[0]
            if self.children[1]:
                self.children[1].parent = self
            for i in range(3):
                r.children[i] = r.children[i + 1]
            r.children[3] = None

        return self.get_root()

    def _merge_with_left(self, l, p, pos):
        # TODO
        
        """与左兄弟合并，父节点中间键下移"""
        count = sum(1 for k in l.keys if k is not None)
        l.keys[count] = p.keys[pos - 1]

        if self.keys[0] is not None:
            l.keys[count + 1] = self.keys[0]

        if not self.is_leaf():
            l.children[count + 1] = self.children[0]
            l.children[count + 2] = self.children[1]
            if l.children[count + 1]:
                l.children[count + 1].parent = l
            if l.children[count + 2]:
                l.children[count + 2].parent = l

        for i in range(pos - 1, 2):
            p.keys[i] = p.keys[i + 1]
        p.keys[2] = None
        for i in range(pos, 3):
            p.children[i] = p.children[i + 1]
        p.children[3] = None

        if p.parent is None and p.keys[0] is None:
            l.parent = None
            return l
        if p.keys[0] is None:
            return p._handle_underflow()
        return p.get_root()

    def _merge_with_right(self, r, p, pos):
        """与右兄弟合并，父节点中间键下移"""
        self.keys[0] = p.keys[pos]
        if r.keys[0] is not None:
            self.keys[1] = r.keys[0]

        if not self.is_leaf():
            self.children[1] = r.children[0]
            self.children[2] = r.children[1]
            if self.children[1]:
                self.children[1].parent = self
            if self.children[2]:
                self.children[2].parent = self

        for i in range(pos, 2):
            p.keys[i] = p.keys[i + 1]
        p.keys[2] = None
        for i in range(pos + 1, 3):
            p.children[i] = p.children[i + 1]
        p.children[3] = None

        if p.parent is None and p.keys[0] is None:
            self.parent = None
            return self
        if p.keys[0] is None:
            return p._handle_underflow()
        return p.get_root()
        pass

    def get_root(self):
        """Returns the root of the tree."""
        current = self
        while current.parent:
            current = current.parent
        return current


def main():
    # --- tests for search ---
    # build tree inline
    root = TwoFourTreeNode()
    nodeA = TwoFourTreeNode()
    nodeB = TwoFourTreeNode()
    leaf0 = TwoFourTreeNode()
    leaf1 = TwoFourTreeNode()
    leaf2 = TwoFourTreeNode()
    leaf3 = TwoFourTreeNode()
    leaf4 = TwoFourTreeNode()

    root.keys = [12, None, None]
    nodeA.keys = [5, 10, None]
    nodeB.keys = [15, None, None]

    leaf0.keys = [3, 4, None]
    leaf1.keys = [6, 7, 8]
    leaf2.keys = [11, None, None]
    leaf3.keys = [13, 14, None]
    leaf4.keys = [17, None, None]

    nodeA.children[0] = leaf0
    nodeA.children[1] = leaf1
    nodeA.children[2] = leaf2
    leaf0.parent = nodeA
    leaf1.parent = nodeA
    leaf2.parent = nodeA

    nodeB.children[0] = leaf3
    nodeB.children[1] = leaf4
    leaf3.parent = nodeB
    leaf4.parent = nodeB

    root.children[0] = nodeA
    root.children[1] = nodeB
    nodeA.parent = root
    nodeB.parent = root

    # tests for found keys
    assert root.search(12) == (root, 0), "12 should be at root[0]"
    assert root.search(5) == (nodeA, 0), "5 should be at nodeA[0]"
    assert root.search(10) == (nodeA, 1), "10 should be at nodeA[1]"
    assert root.search(13) == (leaf3, 0), "13 should be at leaf3[0]"

    # tests for missing keys
    assert root.search(3.2) == (None, -1), "3.2 should not be found"
    assert root.search(20) == (None, -1), "20 should not be found"
    assert root.search(0) == (None, -1), "0 should not be found"
    assert root.search(9) == (None, -1), "9 should not be found"

    print("Search tests passed!")

    # --- tests for delete ---
    # 1. Delete a key from a leaf node
    root = TwoFourTreeNode()
    nodeA = TwoFourTreeNode()
    nodeB = TwoFourTreeNode()
    leaf0 = TwoFourTreeNode()
    leaf1 = TwoFourTreeNode()
    leaf2 = TwoFourTreeNode()
    leaf3 = TwoFourTreeNode()
    leaf4 = TwoFourTreeNode()

    root.keys = [12, None, None]
    nodeA.keys = [5, 10, None]
    nodeB.keys = [15, None, None]

    leaf0.keys = [3, 4, None]
    leaf1.keys = [6, 7, 8]
    leaf2.keys = [11, None, None]
    leaf3.keys = [13, 14, None]
    leaf4.keys = [17, None, None]

    nodeA.children[0] = leaf0
    nodeA.children[1] = leaf1
    nodeA.children[2] = leaf2
    leaf0.parent = nodeA
    leaf1.parent = nodeA
    leaf2.parent = nodeA

    nodeB.children[0] = leaf3
    nodeB.children[1] = leaf4
    leaf3.parent = nodeB
    leaf4.parent = nodeB

    root.children[0] = nodeA
    root.children[1] = nodeB
    nodeA.parent = root
    nodeB.parent = root

    root.delete(4)
    assert root.search(4) == (None, -1), "4 should be deleted from leaf0"

    # 2. Delete a key from an internal node (should replace with predecessor)
    root = TwoFourTreeNode()
    nodeA = TwoFourTreeNode()
    nodeB = TwoFourTreeNode()
    leaf0 = TwoFourTreeNode()
    leaf1 = TwoFourTreeNode()
    leaf2 = TwoFourTreeNode()
    leaf3 = TwoFourTreeNode()
    leaf4 = TwoFourTreeNode()

    root.keys = [12, None, None]
    nodeA.keys = [5, 10, None]
    nodeB.keys = [15, None, None]

    leaf0.keys = [3, 4, None]
    leaf1.keys = [6, 7, 8]
    leaf2.keys = [11, None, None]
    leaf3.keys = [13, 14, None]
    leaf4.keys = [17, None, None]

    nodeA.children[0] = leaf0
    nodeA.children[1] = leaf1
    nodeA.children[2] = leaf2
    leaf0.parent = nodeA
    leaf1.parent = nodeA
    leaf2.parent = nodeA

    nodeB.children[0] = leaf3
    nodeB.children[1] = leaf4
    leaf3.parent = nodeB
    leaf4.parent = nodeB

    root.children[0] = nodeA
    root.children[1] = nodeB
    nodeA.parent = root
    nodeB.parent = root

    root.delete(15)
    assert root.search(15) == (None, -1), "15 should be deleted from nodeB"

    # 3. Delete a key causing a borrow/merge operation
    root = TwoFourTreeNode()
    nodeA = TwoFourTreeNode()
    nodeB = TwoFourTreeNode()
    leaf0 = TwoFourTreeNode()
    leaf1 = TwoFourTreeNode()
    leaf2 = TwoFourTreeNode()
    leaf3 = TwoFourTreeNode()
    leaf4 = TwoFourTreeNode()

    root.keys = [12, None, None]
    nodeA.keys = [5, 10, None]
    nodeB.keys = [15, None, None]

    leaf0.keys = [3, 4, None]
    leaf1.keys = [6, 7, 8]
    leaf2.keys = [11, None, None]
    leaf3.keys = [13, 14, None]
    leaf4.keys = [17, None, None]

    nodeA.children[0] = leaf0
    nodeA.children[1] = leaf1
    nodeA.children[2] = leaf2
    leaf0.parent = nodeA
    leaf1.parent = nodeA
    leaf2.parent = nodeA

    nodeB.children[0] = leaf3
    nodeB.children[1] = leaf4
    leaf3.parent = nodeB
    leaf4.parent = nodeB

    root.children[0] = nodeA
    root.children[1] = nodeB
    nodeA.parent = root
    nodeB.parent = root

    root.delete(6)
    assert root.search(6) == (None, -1), "6 should be deleted causing rebalancing"

    # 4. Delete the root key, causing tree height to decrease
    root = TwoFourTreeNode()
    nodeA = TwoFourTreeNode()
    nodeB = TwoFourTreeNode()
    leaf0 = TwoFourTreeNode()
    leaf1 = TwoFourTreeNode()
    leaf2 = TwoFourTreeNode()
    leaf3 = TwoFourTreeNode()
    leaf4 = TwoFourTreeNode()

    root.keys = [12, None, None]
    nodeA.keys = [5, 10, None]
    nodeB.keys = [15, None, None]

    leaf0.keys = [3, 4, None]
    leaf1.keys = [6, 7, 8]
    leaf2.keys = [11, None, None]
    leaf3.keys = [13, 14, None]
    leaf4.keys = [17, None, None]

    nodeA.children[0] = leaf0
    nodeA.children[1] = leaf1
    nodeA.children[2] = leaf2
    leaf0.parent = nodeA
    leaf1.parent = nodeA
    leaf2.parent = nodeA

    nodeB.children[0] = leaf3
    nodeB.children[1] = leaf4
    leaf3.parent = nodeB
    leaf4.parent = nodeB

    root.children[0] = nodeA
    root.children[1] = nodeB
    nodeA.parent = root
    nodeB.parent = root

    root.delete(12)
    assert root.search(12) == (None, -1), "12 should be deleted and tree height adjusted"

    print("Delete tests passed!")

if __name__ == "__main__":
    main()
