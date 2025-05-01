"""
def binarySearch(arr, target):
    mid = (low + high) // 2
# pass
"""
def product_checker(A, B, m):
    # TODO: Please write your code here
    output = [
    ]
    alreadyseen = set( # 已经出现的 X 去重
    )
    for i in A: #O(n)
        if i == 0 or m % i != 0:
            continue
        target = m // i # 目标必须是整数
        down = 0
        up = len(B) - 1

        # mid = (down + up)//2

        while down <= up: #O(nlogn)
            mid = (down + up) // 2
            if B[mid] == target:
                addee = (i,int(target))

                if addee not in output:
                    alreadyseen.add(addee) # 用set
                    output.append(addee)

                break
            elif B[mid] < target:
                down = mid + 1
            elif B[mid] > target:
                up = mid - 1
    return output
    # pass


# Do not change or remove the code below this point
def main():
    A = [2, 4, 5, 6, 8, 10, 12]
    B = [1, 2, 4, 9, 10, 20]
    print(product_checker(A, B, 40))  # Should print [(2, 20), (4, 10), (10, 4)]

    A = [4, 5, 6, 20]
    B = [1, 2, 4, 10]
    print(product_checker(A, B, 100))  # Should print: []

    A = [1, 2, 2, 3, 5]
    B = [1, 5, 50, 50, 100]
    print(product_checker(A, B, 100))  # Should print: [(1, 100), (2, 50)]


if __name__ == '__main__':
    main()
