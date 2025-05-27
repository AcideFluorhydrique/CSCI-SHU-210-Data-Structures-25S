class Solution:
    def same(self, i1, i2):
        # TODO: Please write your code here
        # i11 = i1[:];i22 = i2[:]
        # i11.sort(); i22.sort()
        # return i11 == i22
        
        # 长度不同 False
        if len(i1) != len(i2):
            return False
        
        if not i1 and not i2:
            return True
        
        elif i1[0] != i2[0]:
            return False
        
        root = i1[0]

        left1 = []
        right1 = []
        left2 = []
        right2 = []
        
        # i1 分割
        for x in i1[1:]:
            if x < root:
                left1.append(x)
            else:
                right1.append(x)
        
        # i2 分割
        for y in i2[1:]:
            if y < root:
                left2.append(y)
            else:
                right2.append(y)
        
        # 检查分割后的子数组长度是否一致
        if (len(left1) != len(left2) or 
            len(right1) != len(right2)
            ):
            return False
        
        # recursion
        if (self.same(left1, left2) and 
            self.same(right1, right2)
            ):
            return True
        
        else:
            return False

def main():
    i1 = [15, 25, 20, 22, 30, 18, 10, 8, 9, 12, 6]
    i2 = [15, 10, 12, 8, 25, 30, 6, 20, 18, 9, 22]

    res = Solution().same(i1, i2)
    print(res)  # Should print true


if __name__ == '__main__':
    main()
