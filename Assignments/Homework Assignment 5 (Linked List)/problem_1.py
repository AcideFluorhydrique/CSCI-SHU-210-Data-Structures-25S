class DoubleLinkedList:
    class Node:
        def __init__(self, element=None, prev=None, next=None):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = DoubleLinkedList.Node(None, None, None)
        self._trailer = DoubleLinkedList.Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = DoubleLinkedList.Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def __str__(self):
        result = "Header<-->"
        currNode = self._header._next
        while currNode is not self._trailer:
            result += str(currNode._element) + "<-->"
            currNode = currNode._next
        return result + "Trailer"

    """
    def reverse(self):
        # TODO: Please write your code here
        for _ in range(self._size - 1):
            process_node = self._delete_node(self._trailer._prev)
            insert_node = self._header
            while _ > 0:
                insert_node = insert_node._next
                _ -= 1
            self._insert_between(process_node, insert_node, insert_node._next)
    """
    def reverse(self):
        curr = self._header
        while curr is not None:
            curr._prev, curr._next = curr._next, curr._prev  # 交换前后指针
            curr = curr._prev  # 由于指针已交换，向前移动

    # 交换 header 和 trailer
        self._header, self._trailer = self._trailer, self._header



def main():
    ls1 = DoubleLinkedList()
    ls1._insert_between(4, ls1._header, ls1._header._next)
    ls1._insert_between(2, ls1._header, ls1._header._next)
    ls1._insert_between(2, ls1._header, ls1._header._next)
    ls1._insert_between(1, ls1._header, ls1._header._next)

    print(ls1)  # Should print: Header<-->1<-->2<-->2<-->4<-->Trailer
    ls1.reverse()
    print(ls1)  # Should print: Header<-->4<-->2<-->2<-->1<-->Trailer


if __name__ == "__main__":
    main()
