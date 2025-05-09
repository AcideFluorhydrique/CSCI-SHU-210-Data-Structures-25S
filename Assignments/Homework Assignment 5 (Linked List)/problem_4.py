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

    def isPalindrome(self):
        if not self._head or not self._head._next:
            return True  # 0 或 1 个节点必定是回文

        # 1. 找到链表的中点（快慢指针）
        slow, fast = self._head, self._head
        prev = None  # 用于反转前半部分链表
        while fast and fast._next:
            fast = fast._next._next
            # 反转前半部分
            next_node = slow._next
            slow._next = prev
            prev = slow
            slow = next_node

        # 2. 处理奇偶链表情况
        first_half_head = prev
        second_half_head = slow if not fast else slow._next  # 如果链表为奇数，跳过中间元素

        # 3. 比较前后两部分是否相等
        is_palindrome = True
        while first_half_head and second_half_head:
            if first_half_head._element != second_half_head._element:
                is_palindrome = False
                break
            first_half_head = first_half_head._next
            second_half_head = second_half_head._next

        return is_palindrome  # 由于我们没有修改后半部分，无需恢复链表

    def _reverseList(self, head):
        """ 反转链表（in-place），返回新的头节点 """
        prev, curr = None, head
        while curr:
            next_node = curr._next
            curr._next = prev
            prev = curr
            curr = next_node
        return prev


def main():
    ls1 = SingleLinkedList()
    ls1.insertAtFirst(1)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(1)

    print(ls1)  # Should print: Head-->1-->2-->2-->1-->None
    print(ls1.isPalindrome())  # Should print: True


if __name__ == "__main__":
    main()
