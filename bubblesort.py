def bubbleSort(mylist):
    for passnum in range(len(mylist)-1,0,-1):
        for i in range(passnum):
            if mylist[i]>mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp
                print "current position = ",mylist

mylist = [1054,26,93,17,707,31,44,55,20]
bubbleSort(mylist)
print(mylist)
