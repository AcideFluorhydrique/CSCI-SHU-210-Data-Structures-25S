def solver(maze):
    # TODO: Please write your code here
    if len(maze) == 0 or len(maze[0]) == 0:
        return []
    elif (maze[0][0] == 0 or
            maze[len(maze) - 1][len(maze[0]) - 1] == 0):
        return []

    def explorer(x, y):
        if (
                x < 0
                or x >= len(maze)
                or y < 0
                or y >= len(maze[0])
                or maze[x][y] == 0
        ):
            return [] # 检查是否可通行

        # Recursion 的 base case
        if (x == len(maze) - 1 and
                y == len(maze[0]) - 1):
            return [(x, y)]
        maze[x][y] = 0   #当前位置直接记为0

        """define the priority of each direction:
           down > right > up > lef"""
        directions = [
            (1, 0), # 下
            (0, 1), # 右
            (-1, 0), # 上
            (0, -1) # left
        ]
        for dx, dy in directions:
            xnew = x + dx
            ynew = y + dy
            path = explorer(xnew, ynew) # recursion
            if path:  #如果找到路径就把当前位置加入path
                return [(x, y)] + path
        return []  # 寄了，无解
    return explorer(0, 0)
# pass


def main():
    res = solver([[1, 0, 1, 1, 1],
                  [1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1],
                  [1, 1, 1, 0, 1]]
    )

    print(res)  # Should print
    # [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4)]

    res = solver([[1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                  [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

    print(res)  # Should print
    # [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4),
    # (0, 4), (0, 5), (0, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (4, 8), (4, 9), (4, 10), (3, 10), (2, 10),
    # (2, 11), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (9, 13), (9, 14)]


if __name__ == '__main__':
    main()
