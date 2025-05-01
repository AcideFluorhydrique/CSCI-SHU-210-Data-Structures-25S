def stock_buy_sell(lissy):
  
    # Assuming input is valid
    # TODO
    start = lissy[0]
    max_d = float('-inf')
    for i in range(1, len(lissy)):
        
        d = lissy[i] - start
        
        if d > max_d:
            max_d = d

        if lissy[i] < start:
            start = lissy[i]
    
    if max_d >0:
        return max_d
    else: return 0
  # return -1


def main():
    l1 = [7,1,5,3,6,4]
    l2 = [7,6,4,3,2,1]

    l3 = [2,9,5,2,3,1,2]
    print(stock_buy_sell(l1)) # expect: 5
    print(stock_buy_sell(l2)) # expect: 0
    print(stock_buy_sell(l3)) # expect: 7

if __name__ == '__main__':
    main()
