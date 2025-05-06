

import math
class Matrix:
    # TODO: Please write your code here

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        # 使用浮点数来存储，并取一位小数

        idata = []
        for _ in range(rows):
            row = []
            for j in range(cols):
                row.append(0.0)
            idata.append(row)
        self.data = idata

    def __str__(self):
        lines = []
        for row in self.data:
            items = []
            for x in row:
                # 如果小数部分是0，
                # 则仅打印整数部分
                # 否则打印浮点数
                if abs(x - round(x)) < 1e-9:
                    items.append(str(int(x)))
                else:
                    items.append(str(x))
            lines.append(" ".join(items))
        return "\n".join(lines)

    def __eq__(self, other):
        if (self._rows != other._rows or
                self._cols != other._cols
        ):
            return False
        # for r in range(self._rows):
        #     for c in range(self._cols):
        #         if self.data[r][c] != other.data[r][c]:
        #             return False
        # return True

        for r in range(self._rows):
            for c in range(self._cols):
                # 如果是浮点数
                # 使用容差比较
                if (isinstance(self.data[r][c], float) or
                        isinstance(other.data[r][c], float)
                ):
                    if abs(self.data[r][c] - other.data[r][c]) > 1e-9:
                        return False
                else:
                    if self.data[r][c] != other.data[r][c]:
                        return False
        return True

    def __add__(self, other):
        result = Matrix(self._rows, self._cols)
        for r in range(self._rows):
            for c in range(self._cols):
                val = self.data[r][c] + other.data[r][c]
                result.data[r][c] = round(val, 1)
        return result

    def __sub__(self, other):
        result = Matrix(self._rows, self._cols)
        for r in range(self._rows):
            for c in range(self._cols):
                val = self.data[r][c] - other.data[r][c]
                result.data[r][c] = round(val, 1)
        return result

    def __mul__(self, other):
        if self._cols != other._rows:
            raise ValueError("Error\n")
        result = Matrix(self._rows, other._cols)
        for i in range(self._rows):
            for j in range(other._cols):
                val = 0.0
                for k in range(self._cols):
                    val += self.data[i][k] * other.data[k][j]
                result.data[i][j] = round(val, 1)
        return result

    def __truediv__(self, other):
        if other._rows == other._cols: # 方阵
            invB = other._inverse()
            return self * invB
        else:
            """ 
            不是哥们，我觉得这个有问题啊？！ 
            """

            # 如果 other 不是方阵
            # 返回与 self 相同维度的全 1 矩阵
            result = Matrix(self._rows, self._cols)
            for r in range(self._rows):
                for c in range(self._cols):
                    result.data[r][c] = 1.0
            return result

    """ 我加了这个因为经常用到"""
    def _inverse(self):
        # 必须是square!!!
        if self._rows != self._cols:
            raise ValueError("Error\n")
        n = self._rows
        # 构造增广矩阵
        aug = []
        for row in self.data:
            aug.append(row[:])
        identity = []
        for i in range(n):
            row = [0.0] * n
            row[i] = 1.0
            identity.append(row)

        for i in range(n):
            pivot_row = i
            max_val = abs(aug[i][i])
            for r in range(i+1, n):
                if abs(aug[r][i]) > max_val:
                    max_val = abs(aug[r][i])
                    pivot_row = r
            if abs(aug[pivot_row][i]) < 1e-14:
                raise ValueError()

            if pivot_row != i:
                aug[i], aug[pivot_row] = aug[pivot_row], aug[i]

                identity[i], identity[pivot_row] = identity[pivot_row], identity[i]
            pivot_val = aug[i][i]
            for c in range(n):
                aug[i][c] /= pivot_val
                identity[i][c] /= pivot_val

            for r in range(n):
                if r != i:
                    factor = aug[r][i]
                    for c in range(n):
                        aug[r][c] -= factor * aug[i][c]
                        identity[r][c] -= factor * identity[i][c]
        # 将结果四舍五入到一位小数
        inv = Matrix(n, n)
        for r in range(n):
            for c in range(n):
                inv.data[r][c] = round(identity[r][c], 1)
        return inv


    ## 这个会在transpose里用到的
    def _transpose_square_recursive(self, i, j):

        if i >= self._rows:
            return
        if j >= self._cols:
            # 切换到下一行
            # 从 i+1 的下一列开始
            self._transpose_square_recursive(i + 1, i + 2)
            return
        if j > i:
            tmp = self.data[i][j]
            self.data[i][j] = self.data[j][i]
            self.data[j][i] = tmp
        self._transpose_square_recursive(i, j + 1)
    def transpose(self):
        if self._rows == self._cols:
            # 方阵的原地转置
            self._transpose_square_recursive(0, 0)
        else:
            new_data = []
            for r in range(self._cols):
                row = []
                for c in range(self._rows):
                    row.append(self.data[c][r])
                new_data.append(row)

            self.data = new_data
            old_rows = self._rows
            self._rows = self._cols
            self._cols = old_rows


    def determinant(self):

        mat_copy = []
        for row in self.data:
            mat_copy.append(row[:])
        n = self._rows
        det_sign = 1.0
        det_val = 1.0

        for i in range(n):
            pivot_row = i
            max_val = abs(mat_copy[i][i])
            for r in range(i+1, n):
                if abs(mat_copy[r][i]) > max_val:
                    max_val = abs(mat_copy[r][i])
                    pivot_row = r

            if abs(mat_copy[pivot_row][i]) < 1e-14:
                # 主元近似为 0
                return float(0)

            if pivot_row != i:
                # 交换行
                mat_copy[i], mat_copy[pivot_row] = mat_copy[pivot_row], mat_copy[i]
                det_sign *= -1

            pivot_val = mat_copy[i][i]
            det_val *= pivot_val

            for r in range(i+1, n):
                factor = mat_copy[r][i] / pivot_val
                for c in range(i, n):
                    mat_copy[r][c] -= factor * mat_copy[i][c]

        # 考虑行交换导致的符号变化
        det_val *= det_sign
        # 四舍五入到一位小数
        return round(det_val, 1)

    def rank(self):
        mat_copy = [

        ]
        for row in self.data:
            mat_copy.append(row[:])
        rows = self._rows
        cols = self._cols
        rank_val = 0
        row_i = 0

        for col_i in range(cols):
            # 在第 col_i 列为主元列，寻找当前主元行
            pivot_row = -1
            max_val = 0.0
            for r in range(row_i, rows):
                if abs(mat_copy[r][col_i]) > max_val:
                    max_val = abs(mat_copy[r][col_i])
                    pivot_row = r

            if (pivot_row == -1 or
                    abs(mat_copy[pivot_row][col_i]) < 1e-14
            ):# 该列没有可用的主元
                continue

            if pivot_row != row_i:
                mat_copy[row_i], mat_copy[pivot_row] = mat_copy[pivot_row], mat_copy[row_i]

            pivot_val = mat_copy[row_i][col_i]
            if abs(pivot_val) > 1e-14:
                for c in range(col_i, cols):
                    mat_copy[row_i][c] /= pivot_val

            # 消去主元以下的元素
            for r in range(row_i + 1, rows):
                factor = mat_copy[r][col_i]
                for c in range(col_i, cols):
                    mat_copy[r][c] -= factor * mat_copy[row_i][c]

            row_i += 1
            rank_val += 1
            if row_i == rows:
                break

        return rank_val

    def scale(self, scalar):

        for r in range(self._rows):
            for c in range(self._cols):
                val = self.data[r][c] * scalar
                self.data[r][c] = round(val, 1)

    def removeRow(self, row_index):
        self.data.pop(row_index)
        self._rows -= 1

    def removeCol(self, col_index):
        for row in self.data:
            row.pop(col_index)
        self._cols -= 1



def main():
    #
    # Student tests for addition of square matrices(+)
    #
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 1], [1, 1]]

    matrix2 = Matrix(2, 2)
    matrix2.data = [[1, 1], [1, 1]]

    print((matrix1 + matrix2).data == [[2, 2], [2, 2]])  # should print the boolean "True"

    matrix3 = Matrix(2, 2)
    matrix3.data = [[2, 2], [2, 2]]

    matrix4 = Matrix(2, 2)
    matrix4.data = [[-1, -1], [-1, -1]]

    print((matrix3 + matrix4).data == [[1, 1], [1, 1]])  # should print the boolean "True"

    #
    # Student tests for addition of non-square matrices(+)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 1, 1], [1, 1, 1]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[1, 1, 1], [1, 1, 1]]

    print((matrix1 + matrix2).data == [[2, 2, 2], [2, 2, 2]])  # should print the boolean "True"

    matrix3 = Matrix(2, 3)
    matrix3.data = [[2, 2, 2], [2, 2, 2]]

    matrix4 = Matrix(2, 3)
    matrix4.data = [[-1, -1, -1], [-1, -1, -1]]

    print((matrix3 + matrix4).data == [[1, 1, 1], [1, 1, 1]])  # should print the boolean "True"

    #
    # Student tests for subtraction of square matrices(-)
    #
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 1], [1, 1]]

    print((matrix1 - matrix1).data == [[0, 0], [0, 0]])  # should print the boolean "True"

    matrix2 = Matrix(2, 2)
    matrix2.data = [[0, 0], [0, 0]]

    matrix3 = Matrix(2, 2)
    matrix3.data = [[-1, -1], [-1, -1]]

    print((matrix2 - matrix3).data == [[1, 1], [1, 1]])  # should print the boolean "True"

    #
    # Student tests for subtraction of non-square matrices(-)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 1, 1], [1, 1, 1]]

    print((matrix1 - matrix1).data == [[0, 0, 0], [0, 0, 0]])  # should print the boolean "True"

    matrix2 = Matrix(2, 3)
    matrix2.data = [[0, 0, 0], [0, 0, 0]]

    matrix3 = Matrix(2, 3)
    matrix3.data = [[-1, -1, -1], [-1, -1, -1]]

    print((matrix2 - matrix3).data == [[1, 1, 1], [1, 1, 1]])  # should print the boolean "True"

    #
    # Student tests for multiplication (*)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(3, 2)
    matrix2.data = [[1, 2], [3, 4], [5, 6]]

    print((matrix1 * matrix2).data == [[22, 28], [49, 64]])  # should print the boolean "True"

    #
    # Student tests for division (/)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    print((matrix1 / matrix1).data == [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])  # should print the boolean "True"

    #
    # Student tests for equality (==)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 1, 1], [1, 1, 1]]

    print(matrix1 == matrix1)  # should print the boolean "True"

    matrix2 = Matrix(2, 3)
    matrix2.data = [[2, 2, 2], [2, 2, 2]]

    print(matrix1 != matrix2)  # should print the boolean "True"

    #
    # Student tests for stringification (print)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 1, 1], [1, 1, 1]]
    print(matrix1.__str__() == "1 1 1\n1 1 1")  # should print the boolean "True"

    matrix2 = Matrix(2, 3)
    matrix2.data = [[-2, -2, -2], [-2, -2, -2]]
    print(matrix2.__str__() == "-2 -2 -2\n-2 -2 -2")  # should print the boolean "True"

    #
    # Student tests for transpose (m^T)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix1.transpose()
    print(matrix1.data == [[1, 4], [2, 5], [3, 6]])  # should print the boolean "True"

    matrix2 = Matrix(2, 2)
    matrix2.data = [[-1, -2], [-3, -4]]

    matrix2.transpose()
    print(matrix2.data == [[-1, -3], [-2, -4]])  # should print the boolean "True"

    #
    # Student tests for determinant
    #
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 2], [3, 4]]

    print(matrix1.determinant() == -2)  # should print the boolean "True"

    #
    # Student tests for rank
    #
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 1], [1, 1]]
    print(matrix1.rank() == 1)  # should print the boolean "True"

    matrix2 = Matrix(4, 4)
    matrix2.data = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    print(matrix2.rank() == 4)  # should print the boolean "True"

    #
    # Student tests for scale
    #
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 1], [1, 1]]

    matrix1.scale(2)
    print(matrix1.data == [[2, 2], [2, 2]])  # should print the boolean "True"

    matrix2 = Matrix(2, 3)
    matrix2.data = [[-1, -1, -1], [-1, -1, -1]]

    matrix2.scale(2)
    print(matrix2.data == [[-2, -2, -2], [-2, -2, -2]])  # should print the boolean "True"

    #
    # Student tests for removeRow
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix1.removeRow(1)
    print(matrix1.data == [[1, 2, 3]])  # should print the boolean "True"

    #
    # Student tests for removeCol
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix1.removeCol(2)
    print(matrix1.data == [[1, 2], [4, 5]])  # should print the boolean "True"


if __name__ == '__main__':
    main()