def selection_sort(L):
    suffixSt=0
    while suffixSt!=len(L):
        for i in range(suffixSt,len(L)):
            print(L)
            if L[i]<L[suffixSt]:
                L[suffixSt],L[i]=L[i],L[suffixSt]
        suffixSt+=1
    return L
testList=[10000,200,3,59,74,91,18,27]
print(selection_sort(testList))