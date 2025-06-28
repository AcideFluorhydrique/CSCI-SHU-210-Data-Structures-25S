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
        # TODO: Please write your code here

        for i, current_key in enumerate(self.keys):
            if current_key == key:
                return (self, i)  # Key found in current node
        
        if self.is_leaf():
            return (None, -1)
        
        # Determine which child to search
        if (self.keys[0] is None or 
            key < self.keys[0]
            ):

            if self.children[0] is not None:
                return self.children[0].search(key)
        elif (self.keys[1] is None or 
              key < self.keys[1]
              ):
            
            if self.children[1] is not None:
                return self.children[1].search(key)
        elif (self.keys[2] is None or 
              key < self.keys[2]
              ):
            
            if self.children[2]:
                return self.children[2].search(key)
        else:
            if self.children[3]:
                return self.children[3].search(key)
        
        return (None, -1)
        pass


def main():
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

    # --- tests for found keys ---
    assert root.search(12) == (root, 0), "12 should be at root[0]"
    assert root.search(5) == (nodeA, 0), "5 should be at nodeA[0]"
    assert root.search(10) == (nodeA, 1), "10 should be at nodeA[1]"
    assert root.search(13) == (leaf3, 0), "13 should be at leaf3[0]"

    # --- tests for missing keys ---
    assert root.search(3.2) == (None, -1), "3.2 should not be found"
    assert root.search(20) == (None, -1), "20 should not be found"
    assert root.search(0) == (None, -1), "0 should not be found"
    assert root.search(9) == (None, -1), "9 should not be found"

    print("All tests passed!")


if __name__ == "__main__":
    main()
