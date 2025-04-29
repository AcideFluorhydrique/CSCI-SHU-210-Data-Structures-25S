# def dec2bin(d):
#     pass

"""这道题只能用位运算"""
def flip_bit(num, bit_position):
    # TODO: Please write your code here
    if bit_position == 0:
        return num ^ 1
    answer = num ^ (2 << (bit_position - 1)) # 这道题不能用python运算
    return answer

    # pass


# Do not change or remove the code below this point
def main():
    print(flip_bit(8, 1))  # Expected Output: 10
    print(flip_bit(10, 1))  # Expected Output: 8

    # print(flip_bit(8, 2))  # Expected Output: 10
    # print(flip_bit(10, 3))  # Expected Output: 8

if __name__ == "__main__":
    main()

