def count_connected(voxel_grid):
    # TODO: Please write your code here
    Z = len(voxel_grid)
    Y = len(voxel_grid[0])
    X = len(voxel_grid[0][0])

    visited = [

    ]
    for _ in range(Z):
        layer = []
        for __ in range(Y):
            r = [False] * X
            layer.append(r)
        visited.append(layer)

    # 这是深度优先搜索dfs遍历连通区域
    def dfs(z, y, x):
        visited[z][y][x] = True

        neighbours = [ # 这是6个方向
            (z + 1, y, x),
            (z - 1, y, x),
            (z, y + 1, x),
            (z, y - 1, x),
            (z, y, x + 1),
            (z, y, x - 1)
        ]

        for nz, ny, nx in neighbours:
            # 边界
            if (0 <= nz < Z and
                    0 <= ny < Y and
                    0 <= nx < X
            ): # 若邻居体素值为1且未被访问过就递归调用dfs
                if (voxel_grid[nz][ny][nx] == 1 and
                        not visited[nz][ny][nx]
                ):
                    dfs(nz, ny, nx)

    c = 0

    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                # if体素值为1且未被访问过，
                # 说明我找到了一个新的连通区域
                if (voxel_grid[z][y][x] == 1 and
                        not visited[z][y][x]
                ):
                    c += 1
                    dfs(z,
                        y,
                        x
                    ) # 从当前体素开始进行深度优先搜索
    return c
    # pass


def visualise(voxel_grid):
    """
    This is a given method for visualising a provided voxel-grid.
    You can not change this function.
    """
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(np.array(voxel_grid))
    plt.show()


def main():
    # multidimensional representation of a single voxel.
    single_cube = [
        [
            [1]
        ]
    ]
    """ Here """
    """ 这里 """
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(single_cube)
    print(count_connected(single_cube))  # Should print the integer "1"

    # multidimensional representation of two cube-like components.
    two_cube_like_components = [
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ], [
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(two_cube_like_components)
    print(count_connected(two_cube_like_components))  # Should print the integer "2"

    # multidimensional representation of 6 bars in diagonal.
    six_bars = [
        [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]
        ],
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1]
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(six_bars)
    print(count_connected(six_bars))  # Should print the integer "6"

    # multidimensional representation of 3 connected blocks.
    connected_blocks = [
        [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(connected_blocks)
    print(count_connected(connected_blocks))  # Should print the integer "1"

    # multidimensional representation of 2 bars.
    two_bars = [
        [
            [1, 0],
        ], [
            [0, 1],
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(two_bars)
    print(count_connected(two_bars))  # Should print the integer "2"

    # multidimensional representation of 2 bars (2).
    two_bars_2 = [
        [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
        ], [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ], [
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1],
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(two_bars_2)
    print(count_connected(two_bars_2))  # Should print the integer "2"

    # multidimensional representation of 3 connected componentes.
    connected_3 = [
        [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
        ], [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ], [
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1],
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(connected_3)
    print(count_connected(connected_3))  # Should print the integer "3"

    # multidimensional representation of a partial wireframe.
    partial_wireframe = [
        [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ], [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ], [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ], [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ], [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
        ], [
            [1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ]
    ]
    # Uncomment the following line of code to visualise the 3d-array using matplotlib.
    # You need to comment this line when submitting your solution to gradescope to prevent errors.
    # visualise(partial_wireframe)
    print(count_connected(partial_wireframe))  # Should print the integer "1"


if __name__ == "__main__":
    main()
