#bisection search implementation1    #O(nlog(n))
def bisect_search_1(L,e):
    if L==[]:
        return False
    elif len(L)==1:
        return L[0]==e
    else:
        half = len(L)//2
        if L[half]>e:
            return bisect_search_1(L[:half],e)#O(log(n))
        else:
            return bisect_search_1(L[half:],e)#O(log(n))
        
#Bisection search implementation2        #O(log(n))
def bisect_search_2(L,e):
    def bisect_search_helper(L,e,low,high):
        if high == low:
            return L[low]==e
        mid=(low+high//2)
        if L[mid]==e:
            return True
        elif L[mid]>e:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L,e,low,mid-1)
        else:
            return bisect_search_helper(L,e,mid+1,high)
    if len(L)==0:
        return False
    else:
        return bisect_search_helper(L,e,0,len(L)-1)    
            

testList=[1,2,3,5,7,9,18,27]
print(bisect_search_1(testList,9))
print(bisect_search_2(testList,5))