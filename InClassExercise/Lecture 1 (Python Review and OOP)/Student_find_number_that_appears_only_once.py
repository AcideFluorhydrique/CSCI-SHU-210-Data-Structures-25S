def find(lissy):
    # TODo
    temp = []
    for i in lissy:
        if i not in temp:
            temp.append(i)
        else:
            temp.remove(i)
    return temp[0]

    # for i in range(len(lissy)):
    #     if lissy.count(lissy[i]) == 1:
    #         return lissy[i]

    # return -1

def main():
    l1 = [7,1,5,3,6,4,7,1,5,6,4]
    l2 = [7,6,4,3,2,1,1,2,3,4,5,6,7]
    print(find(l1)) # expect: 3
    print(find(l2)) # expect: 5

if __name__ == '__main__':
    main()
