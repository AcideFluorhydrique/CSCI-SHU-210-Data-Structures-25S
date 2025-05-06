def yield_func(a):
    print("Start")
    yield a + 1
    print("Middle")
    yield a + 2
    print("End")

# 创建生成器对象，但不会执行函数体
gen = yield_func(10)

# 第一次 next()，执行到第一个 yield
print(next(gen))  # 输出 "Start"，返回 11

# 第二次 next()，继续执行到下一个 yield
print(next(gen))  # 输出 "Middle"，返回 12

# 第三次 next()，函数结束
print(next(gen))  # 输出 "End"，抛出 StopIteration 异常


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def is_palindrome(queue):
    stack = []
    size = 0

    # 将队列元素复制到栈中，并恢复队列原顺序
    while not queue.is_empty():
        elem = queue.dequeue()
        stack.append(elem)
        queue.enqueue(elem)
        size += 1

    # 比较队列元素与栈中元素
    result = True
    for _ in range(size):
        elem = queue.dequeue()
        stack_elem = stack.pop()
        if elem != stack_elem:
            result = False
        queue.enqueue(elem)

    return result


# 示例测试
q = Queue()
for num in [1, 2, 3, 2, 1]:
    q.enqueue(num)
print(is_palindrome(q))  # 输出: True

while not q.is_empty():
    print(q.dequeue(), end=' ')  # 输出: 1 2 3 2 1，队列顺序保持不变
# 示例测试
q = Queue()
for num in [1, 2, 3, 3, 2, 1]:
    q.enqueue(num)
print(is_palindrome(q))  # 输出: True

# 验证队列顺序
restored = []
while not q.is_empty():
    restored.append(q.dequeue())
print(restored)  # 输出: [1, 2, 3, 3, 2, 1]