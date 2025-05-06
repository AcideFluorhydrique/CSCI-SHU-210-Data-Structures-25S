class Node:
    def __init__(self, element, next=None):
        self._element = element  # 可以是基本类型或 Single_Linked_List 对象
        self._next = next        # 指向同一层级的下一个节点

class Single_Linked_List:
    def __init__(self):
        self._head = None  # 链表头部
        self._size = 0     # 主链表中的节点数量

    def __str__(self):
        def print_node(node):
            if not node:
                return ""
            # 如果 _element 是嵌套链表，用方括号括起来
            if isinstance(node._element, Single_Linked_List):
                result = "[" + str(node._element) + "]"
            else:
                result = str(node._element)
            # 如果有下一个节点，添加空格并递归打印
            if node._next:
                result += " " + print_node(node._next)
            return result
        return print_node(self._head).strip()

def convert_nested_list(nested_list):
    def build_list(lst):
        if not lst:
            return None, 0
        head = None
        tail = None
        size = 0
        for item in lst:
            if isinstance(item, list):
                # 递归构建嵌套链表
                sub_list = convert_nested_list(item)
                new_node = Node(sub_list)
            else:
                new_node = Node(item)
            if not head:
                head = new_node
                tail = new_node
            else:
                tail._next = new_node
                tail = new_node
            size += 1
        return head, size

    linked_list = Single_Linked_List()
    head, size = build_list(nested_list)
    linked_list._head = head
    linked_list._size = size
    return linked_list



# 测试 1：简单嵌套
nested_list = ['a', ['b', 'c'], 'd', ['e'], 'f']
nested_linked_list = convert_nested_list(nested_list)
print(nested_linked_list)  # 输出：a [b c] d [e] f

# 测试 2：多层嵌套
nested_list2 = [['a', 'b'], ['c', ['d', 'e']]]
nested_linked_list2 = convert_nested_list(nested_list2)
print(nested_linked_list2)  # 输出：[a b] [c [d e]]

# 这是gpt回忆的