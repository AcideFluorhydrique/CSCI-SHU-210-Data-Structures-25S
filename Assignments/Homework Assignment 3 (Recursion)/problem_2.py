def knapsack_recursive(weights, values, capacity, n):
    # TODO: Please write your code here

    # 0/1 背包问题
    if n <= 0 or capacity <= 0:
        return 0;

    elif weights[n - 1] > capacity:
        return knapsack_recursive(weights, values, capacity, n - 1)

    return max(
        # 不包含第 n 个物品 (python 的 index 是 n - 1)
        knapsack_recursive(weights, values, capacity, n - 1),

        # 包含第 n 个物品
        (values[n - 1] +
         knapsack_recursive(
             weights, values, capacity - weights[n - 1], n - 1
             )
         )
    )
    # pass


def main():
    weights, values = [1, 3, 4, 5], [1, 4, 5, 7]
    capacity, n = 7, len(weights)
    result = knapsack_recursive(weights, values, capacity, n)
    print(result)  # Should print: 9 because of weights four and five with value 5 and 7


if __name__ == '__main__':
    main()