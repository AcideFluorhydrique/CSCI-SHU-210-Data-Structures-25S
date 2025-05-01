def findMedianSortedArrays(nums1, nums2):
    # TODO: Please write your code here
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)
    m, n = len(nums1), len(nums2)
    total = m + n

    if m == 0:
        if n % 2 == 0:
            return (nums2[total / 2] + nums2[total / 2 - 1]) / 2
        else:
            return nums2[total // 2]

    lefthalf = (total + 1) // 2  # 左边的总长度和奇偶无关

    low = 0
    high = m
    while low <= high:
        i = (low + high) // 2  # i是nums1的分割点
        j = lefthalf - i  # j是nums2的分割点
        """
        处理边界情况
        如果 i > 0，左半部分的最大值是 nums1[i-1]
        如果 i = 0，左半部分为空，负∞
        如果 i < m，右半部分的最小值是 nums1[i]
        如果 i = m，右半部分空，∞

        如果 j > 0，左半部分的最大值是 nums2[j-1]
        如果 j = 0，左半部分空，负∞
        如果 j < n，右半部分的最小值是 nums2[j]
        如果 j = n，右半部分空，∞
        """
        if i > 0:
            left1 = nums1[i - 1]
        else:
            left1 = float('-inf')
        if j > 0:
            left2 = nums2[-1 + j] # 左
        else:
            left2 = float('-inf')
        if i < m:
            right1 = nums1[i]
        else:
            right1 = float("inf")
        if j < n:
            right2 = nums2[j]
        else:
            right2 = float('inf')

        if left1 <= right2 and left2 <= right1:
            if total % 2 == 1:
                return max(left1, left2)
            else:
                return (max(left1, left2) + min(right1, right2)) / 2
        elif left1 > right2:
            high = i - 1
        else:
            low = i + 1
    return 0;
    # pass


# Do not change or remove the code below this point
def main():
    # Example 1
    nums1 = [1, 3,
             5, 7
             ]
    nums2 = [2]
    result = findMedianSortedArrays(nums1, nums2)
    print(result)  # Should print 3

    # Example 2
    nums1 = [1, 2]
    nums2 = [4, 5]
    result = findMedianSortedArrays(nums1, nums2)
    print(result)  # Median is (2 + 4) / 2 = 3.0
    # Should print 3


if __name__ == '__main__':
    main()