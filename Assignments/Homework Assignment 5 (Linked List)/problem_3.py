class SingleLinkedList:
    class Node:
        def __init__(self, element=None, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insertAtFirst(self, e):
        newNode = self.Node(e, self._head)
        self._head = newNode
        self._size += 1

    def deleteFirst(self):
        if self.is_empty():
            raise Exception('LinkedList is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def deleteLast(self):
        if self.is_empty():
            raise Exception('LinkedList is empty')
        prv = None
        cur = self._head
        while cur._next is not None:
            cur = cur._next
            prv = prv._next if prv is not None else self._head
        if prv is None:
            self._head = None
        else:
            prv._next = None
        self._size -= 1
        return cur._element

    def unOrderedSearch(self, target):
        currNode = self._head
        while currNode is not None and currNode._element != target:
            currNode = currNode._next
        return currNode is not None

    def __str__(self):
        result = "Head-->"
        currNode = self._head
        while currNode is not None:
            result += str(currNode._element) + "-->"
            currNode = currNode._next
        return result + "None"

    def sortList(self):
        if self._size <= 1:
            return  # 空链表或只有一个元素，无需排序
        pivot = self._choosePivot()
        left, pivot_list, right = self._partition(pivot)
        left.sortList()
        right.sortList()
        self._concat(left, pivot_list, right)

    def _choosePivot(self):
        # 三数取中法选择 pivot，确保不包含 None
        first = self._head._element if self._head else None
        last = self._getLastElement() if self._head else None
        middle = self._findMiddle() if self._head else None

        # 过滤掉 None 值，只保留有效元素
        valid_values = [x for x in [first, middle, last] if x is not None]

        if len(valid_values) == 0:
            raise Exception("Cannot select pivot from an empty list")
        elif len(valid_values) == 1:
            pivot = valid_values[0]
        elif len(valid_values) == 2:
            pivot = min(valid_values)  # 如果只有两个数，选较小的防止极端情况
        else:
            pivot = sorted(valid_values)[1]  # 取三数中位数

        return pivot

    def _getLastElement(self):
        """返回链表最后一个元素"""
        if not self.is_empty():
            current = self._head
            while current._next:
                current = current._next
            return current._element
        return None

    def _findMiddle(self):
        """使用快慢指针找到中间值"""
        if self.is_empty():
            return None
        slow = self._head
        fast = self._head
        while fast and fast._next:
            slow = slow._next
            fast = fast._next._next
        return slow._element

    def _partition(self, pivot):
        """根据 pivot 进行 partition，返回两个新链表"""
        left = SingleLinkedList()
        right = SingleLinkedList()
        pivot_list = SingleLinkedList()

        curr = self._head
        while curr:
            next_node = curr._next  # 记录下一个节点
            if curr._element < pivot:
                left.insertAtFirst(curr._element)
            elif curr._element > pivot:
                right.insertAtFirst(curr._element)
            else:
                pivot_list.insertAtFirst(curr._element)
            curr = next_node
        return left, pivot_list, right

    def _concat(self, left, pivot_list, right):
        """合并 left + pivot_list + right"""
        if left._head is None:
            self._head = pivot_list._head
        else:
            # 找到 left 的尾部
            curr = left._head
            while curr._next:
                curr = curr._next
            curr._next = pivot_list._head
            self._head = left._head

        # 找到 pivot_list 的尾部
        if pivot_list._head:
            curr = pivot_list._head
            while curr._next:
                curr = curr._next
            curr._next = right._head
        else:
            if left._head:
                curr._next = right._head
            else:
                self._head = right._head
    

    """
    def sortList(self):
        # TODO: Please write your code here
        if self._size <= 1:
            return  # 空链表或只有一个元素，无需排序

        pivot = self._choosePivot()
        left, pivot_list, right = self._partition(pivot)

        left.sortList()
        right.sortList()

        self._concat(left, pivot_list, right) 

    def _findMiddle(self):
        #使用快慢指针找到中间值
        if self.is_empty():
            return None
        slow, fast = self._head, self._head
        prev = None  # 记录 slow 的前一个节点
        while fast and fast._next:
            prev = slow
            slow = slow._next
            fast = fast._next._next

            # 从链表中删除 middle
        if prev:
            prev._next = slow._next

        return slow._element if slow else None

    def _choosePivot(self):
        #三数取中法选择 pivot，确保不包含 None
        first = self.deleteFirst() if not self.is_empty() else None
        last = self.deleteLast() if not self.is_empty() else None
        middle = self._findMiddle() if not self.is_empty() else None

        # 过滤掉 None 值，只保留有效元素
        valid_values = [x for x in [first, middle, last] if x is not None]

        # 选取中位数作为 pivot
        if len(valid_values) == 0:
            raise Exception("Cannot select pivot from an empty list")
        elif len(valid_values) == 1:
            pivot = valid_values[0]
        elif len(valid_values) == 2:
            pivot = min(valid_values)  # 如果只有两个数，选较小的防止极端情况
        else:
            pivot = sorted(valid_values)[1]  # 取三数中位数
        # 重新插入 first、middle、last（只插入非 None 值）
        if first is not None:
            self.insertAtFirst(first)
        if last is not None:
            self.insertAtFirst(last)
        if middle is not None:
            self.insertAtFirst(middle)

        return pivot

    def _partition(self, pivot):
        #根据 pivot 进行 partition，返回两个新链表
        left = SingleLinkedList()
        right = SingleLinkedList()
        pivot_list = SingleLinkedList()

        curr = self._head
        while curr:
            next_node = curr._next  # 记录下一个节点
            if curr._element < pivot:
                left.insertAtFirst(curr._element)
            elif curr._element > pivot:
                right.insertAtFirst(curr._element)
            else:
                pivot_list.insertAtFirst(curr._element)
            curr = next_node

        return left, pivot_list, right

    def _concat(self, left, pivot_list, right):
        #合并 left + pivot_list + right
        if left._head is None:
            self._head = pivot_list._head
        else:
            # 找到 left 的尾部
            curr = left._head
            while curr._next:
                curr = curr._next
            curr._next = pivot_list._head
            self._head = left._head

        # 找到 pivot_list 的尾部
        if pivot_list._head:
            curr = pivot_list._head
            while curr._next:
                curr = curr._next
            curr._next = right._head
        else:
            if left._head:
                curr._next = right._head
            else:
                self._head = right._head
    """


def main():
    ls1 = SingleLinkedList()
    ls1.insertAtFirst(3)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(6)
    ls1.insertAtFirst(5)

    print(ls1)  # Should print: Head-->5-->6-->2-->3-->None
    ls1.sortList()
    print(ls1)  # Should print: Head-->2-->3-->5-->6-->None

    ls2 = SingleLinkedList()
    ls2.insertAtFirst(9)
    ls2.insertAtFirst(1)
    ls2.insertAtFirst(5)
    ls2.insertAtFirst(4)
    ls2.insertAtFirst(3)
    ls2.insertAtFirst(2)
    ls2.insertAtFirst(5)
    ls2.insertAtFirst(6)
    ls2.insertAtFirst(1)
    ls2.sortList()
    print(ls2)


if __name__ == "__main__":
    main()
