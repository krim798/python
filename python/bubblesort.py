def bubble_sort(L):
    swap= False
    while not swap:
        swap = True
        for j in range(1,len(L)):
            if L[j-1]>L[j]:
                swap=False
                temp=L[j]
                L[j]=L[j-1]
                L[j-1]=temp
    return L
testList=[10000,200,3,59,74,91,18,27]
print(bubble_sort(testList))