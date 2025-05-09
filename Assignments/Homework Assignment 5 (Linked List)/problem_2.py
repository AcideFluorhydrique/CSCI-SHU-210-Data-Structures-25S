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
    def rotate(self, n):
        # TODO: Please write your code here
        for _ in range(n):
            process_node = self._delete_node(self._trailer._prev)
            insert_node = self._header
            self._insert_between(process_node, insert_node, insert_node._next)
    """
    def rotate(self, n):
        if self.is_empty() or n <= 0:
            return
    
        n = n % self._size  # 避免多余旋转
        for _ in range(n):
            last_node = self._trailer._prev  # 取出最后一个节点
            last_element = last_node._element  # 获取元素
            self._delete_node(last_node)  # 删除最后一个节点
            self._insert_between(last_element, self._header, self._header._next)  # 插入头部  # 插入头部
            


def main():
    ls1 = DoubleLinkedList()
    ls1._insert_between(5, ls1._header, ls1._header._next)
    ls1._insert_between(4, ls1._header, ls1._header._next)
    ls1._insert_between(3, ls1._header, ls1._header._next)
    ls1._insert_between(2, ls1._header, ls1._header._next)
    ls1._insert_between(1, ls1._header, ls1._header._next)

    print(ls1)  # Should print: Header<-->1<-->2<-->3<-->4<-->5<-->Trailer
    ls1.rotate(2)
    print(ls1)  # Should print: Header<-->4<-->5<-->1<-->2<-->3<-->Trailer


if __name__ == "__main__":
    main()
