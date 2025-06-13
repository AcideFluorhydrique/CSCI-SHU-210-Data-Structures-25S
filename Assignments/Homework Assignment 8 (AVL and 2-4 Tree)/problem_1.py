class TwoFourTreeNode:
    def __init__(self):
        self.keys = [None] * 3
        self.children = [None] * 4
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
                if self.is_leaf() or self.children[i] is None:
                    return None, -1
                return self.children[i].search(key)

        if self.is_leaf() or self.children[count] is None:
            return None, -1
        return self.children[count].search(key)

    def insert(self, key):
        def root(node):
            while node.parent:
                node = node.parent
            return node

        def is_overflow(node):
            return sum(1 for k in node.keys if k is not None) > 3

        def insert_key(node, key):
            ks = [

            ]
            for k in node.keys:
                if k is not None:
                    ks.append(k)
            ks.append(key)
            ks.sort()
            while len(ks) < 4:
                ks.append(None)
            node.keys = ks

        def split(node):
            ks = [

            ]
            for k in node.keys:
                if k is not None:
                    ks.append(k)
            if len(ks) != 4:
                raise Exception('')

            mid = ks[2]
            l = TwoFourTreeNode()
            r = TwoFourTreeNode()
            l.keys = [ks[0], ks[1], None]
            r.keys = [ks[3], None, None]

            # 如果有子节点，则分配子节点
            if any(node.children):
                l.children = [None] * 4
                r.children = [None] * 4
                # 左边节点获取原节点的第0~2号子节点，右边获取第3~4号子节点
                for i in range(3):
                    if i < len(node.children):
                        l.children[i] = node.children[i]
                        if l.children[i]:
                            l.children[i].parent = l
                for i in range(3, 5):
                    if i < len(node.children):
                        r.children[i - 3] = node.children[i]
                        if r.children[i - 3]:
                            r.children[i - 3].parent = r

            if node.parent is None:
                new_root = TwoFourTreeNode()
                new_root.keys = [mid, None, None]
                new_root.children = [l, r, None, None]
                l.parent = new_root
                r.parent = new_root
                return new_root
            else:
                p = node.parent
                idx = p.child_index(node)
                insert_key(p, mid)
                p.children[idx] = l
                p.children.insert(idx + 1, r)
                l.parent = p
                r.parent = p
                # 移除多余的子节点（None）
                filtered_children = [

                ]
                for c in p.children:
                    if c is not None:
                        filtered_children.append(c)
                p.children = filtered_children
                while len(p.children) < 4:
                    p.children.append(None)
                if is_overflow(p):
                    return split(p)
                else:
                    return root(p)

        # 如果已有该 key，直接返回
        if self.search(key) != (None, -1):
            return self

        curr = root(self)
        # 向下查找插入位置
        while not curr.is_leaf():
            valid_keys = [k for k in curr.keys if k is not None]
            idx = 0
            while idx < len(valid_keys) and key > valid_keys[idx]:
                idx += 1
            if curr.children[idx] is None:
                break
            curr = curr.children[idx]

        # 插入 key 到叶子节点
        insert_key(curr, key)

        # 如果插入后超出限制，则进行分裂
        if is_overflow(curr):
            return split(curr)
        else:
            return root(curr)

        # pass


def main():
    keys = [12, 5, 10, 15, 3, 4, 6, 7, 8, 11, 13, 14, 17]
    root = TwoFourTreeNode()
    for k in keys:
        # print(f'inserting {k}...')
        root = root.insert(k)

    # --- tests for found keys ---
    assert root.search(12) == (root, 0), "12 should be at root[0]"
    assert root.search(5)[0].keys[0] == 5, "5 should be in left child"
    assert root.search(11)[0].keys[1] == 11, "11 should be in left child"
    assert root.search(13)[0].keys[0] == 13, "13 should be in middle/right leaf"

    # --- tests for missing keys ---
    assert root.search(3.2) == (None, -1), "3.2 should not be found"
    assert root.search(20) == (None, -1), "20 should not be found"
    assert root.search(0) == (None, -1), "0 should not be found"
    assert root.search(9) == (None, -1), "9 should not be found"

    print("All tests passed!")


if __name__ == "__main__":
    main()
