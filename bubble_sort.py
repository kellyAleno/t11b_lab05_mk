
def bubbleSort(alist):

    for a in range(len(alist)-1,0,-1):
        for i in range(a):
            change = 0
            if alist[i]>alist[i+1]:
                change = 1
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            if change == 1:
                print(alist)

            print (type(alist[1]))


list = input("Insert a list of numbers seperated by spaces to be sorted\n")
new_list = [int(n) for n in list.split(',')]
bubbleSort(new_list)