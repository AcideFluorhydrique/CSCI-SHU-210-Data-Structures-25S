def subsets(s):
    # TODO: Please write your code here
    if s == []:
        return [[]]

    first = s[0]
    others = s[1:]
    nofirst = subsets(others)

    withfirst = [

    ]
    for i in nofirst:
        withfirst.append([first] + i)

    return withfirst + nofirst
    # pass


def main():
    print(subsets(["A", "B", "C"]))  # Should print:
    # [[], ['C'], ['B'], ['B', 'C'], ['A'], ['A', 'C'], ['A', 'B'], ['A', 'B', 'C']]

    print(subsets(["K", "L", "M", "Z"]))  # Should print:
    # [[], ['Z'], ['M'], ['M', 'Z'], ['L'], ['L', 'Z'], ['L', 'M'], ['L', 'M', 'Z'], ['K'], ['K', 'Z'], ['K', 'M'],
    # ['K', 'M', 'Z'], ['K', 'L'], ['K', 'L', 'Z'], ['K', 'L', 'M'], ['K', 'L', 'M', 'Z']]


if __name__ == '__main__':
    main()
