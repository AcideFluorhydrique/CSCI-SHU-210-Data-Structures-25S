import timeit
import random

def timeFunction(f,n,repeat=1):
	return timeit.timeit(f.__name__+'('+str(n)+')',setup="from __main__ import "+f.__name__,number=repeat)/repeat

def insertion_sort(data_list):
    # 1. Split data into two parts: sorted & unsorted
    #    X | X X X X X X X
    #    sorted | unsorted
    # 2. While size of unsorted part is greater than zero锛?    
    #   a. let the target element be the first element in the unsorted part
    #   b. find targets insertion point in the sorted part
    #   c. make place at insertion point by shifting all larger elements
    #   d. insert the target in its final, sorted position

    # Coding: Please sort the values in-place, i.e. no new data_list is created and final sorted values are in data_list
    # for j in range(len(data_list)):
    #     srt = data_list[0:j]
    #     unsrt = data_list[j:]
    #     i=0
    #     for _ in range(len(srt)):
    #         if unsrt[0]< srt[_]:
    #             i += 1
    #         else:
    #             break
    #     srt.insert(i,unsrt[0])
    #     unsrt.pop(0)
    # data_list = srt + unsrt


    for j in range(len(data_list)):
        key = data_list[j]
        i = j -1
        while i >= 0 and data_list[i] > key:
            data_list[i + 1] = data_list[i]
            i -= 1
        data_list[i + 1] = key
    return data_list

    # pass

def python_sort(data_list):
    # Use list.sort()
    # Python built in sort uses Tim-sort
    data_list.sort()
    return data_list
    # pass

if __name__ == '__main__':
    data1 = []
    data2 = []
    for i in range(10000):
        value = random.randint(0,1000)
        data1.append(value)
        data2.append(value)



    print("Insertion sort 10000 elements:",
          '{:.6f}'.format(timeFunction(insertion_sort, data1)), "seconds")
    print("Built in sort 10000 elements:",
          '{:.6f}'.format(timeFunction(python_sort, data2)), "seconds")
          
    # insertion_sort(data1)
    # data2.sort()
    # print(data1);print(data2)
