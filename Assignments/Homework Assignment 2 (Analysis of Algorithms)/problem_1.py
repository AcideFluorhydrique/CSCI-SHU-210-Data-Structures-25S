def find_nearest_temperature(sorted_temps, target_temp):
    # TODO: Please write your code here
    down = 0
    up = len(sorted_temps) - 1
    if len(sorted_temps) == 0:
        return None
    # test_10_empty_list (test1.TestForProblem1)
    # None 空列表！！！
    elif len(sorted_temps) == 1:
        return sorted_temps[0]
    mid = (up + down) //2

    while up - down >1:
        mid = (up + down) // 2
        if sorted_temps[mid] > target_temp:
            up = mid
        elif sorted_temps[mid] < target_temp:
            down = mid
        elif sorted_temps[mid] == target_temp:
            return sorted_temps[mid]
    result = []
    result.append(sorted_temps[up])
    result.append(sorted_temps[down])
    if target_temp - result[1] > result[0] - target_temp:
        return result[0]
    else: return result[1]
    # pass


# Do not change or remove the code below this point
def main():
    sorted_temps = [-20, -15, -5, 3, 8, 12, 30, 45, 50, 60]
    target_temp = 7

    nearest = find_nearest_temperature(sorted_temps, target_temp)
    print(nearest)  # Should print 8


if __name__ == "__main__":
    main()
