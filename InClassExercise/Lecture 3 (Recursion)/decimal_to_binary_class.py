# Suppose n is a positive integer, n >= 0 .
# Convert n to its binary representation without using any library function.

# def findlength(n):
#     length = 0
#     while n > 0:
#         length += 1
#         n >>= 1
#     return length


def recursive_decimal_to_binary_str(n):
    # To do
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    return recursive_decimal_to_binary_str(n // 2) + str(n % 2)
    # pass

def main():
    print(recursive_decimal_to_binary_str(6)) #110
    print(recursive_decimal_to_binary_str(13)) #1101
    print(recursive_decimal_to_binary_str(126)) #1111110
    print(recursive_decimal_to_binary_str(509)) #111111101
    
	
if __name__ == '__main__':
    main()

