def special_generator(n):
    # TODO: Please write your code here
    for i in range(1, 1 + n):
        if i % 4 == 0 and i % 6 != 0:
            # print("GYUFGUFGUIKGYU")
            yield "Quad"
        elif i % 6 == 0 and i % 4 != 0:
            yield "Hex"
        elif i % 4 == 0 and i % 6 == 0:
            yield "QuadHex"
        else: yield i
    # pass

# Do not change or remove the code below this point
def main():
    gen = special_generator(15)
    print(list(gen))  # Expected Output: [1, 2, 3, 'Quad', 5, 'Hex', 7, 'Quad', 9, 10, 11, 'QuadHex', 13, 14, 15]

if __name__ == "__main__":
    main()
