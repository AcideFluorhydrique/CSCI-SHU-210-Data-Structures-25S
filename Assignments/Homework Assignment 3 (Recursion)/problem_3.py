def expression(numbers):
    # TODO: Please write your code here
    if len(numbers) == 1:
        return [
            str(numbers[0])
        ]

    # 除了首项以外的可以用recursion先写出来
    previous = expression(numbers[1:])
    output = [
    ]
    for i in previous:
        output.append(str(numbers[0]) +"*"+ i)
        output.append(str(numbers[0]) +"+"+ i)
        output.append(str(numbers[0]) +"-"+ i)
    return output

def main():
    print(expression([1, 2, 3]))  # Should print: ['1-2*3', '1+2+3', '1-2-3', '1*2*3', '1-2+3', '1+2*3', '1+2-3', '1*2+3', '1*2-3']
    print(expression([8, 9]))  # Should print: ['8+9', '8*9', '8-9']


if __name__ == '__main__':
    main()