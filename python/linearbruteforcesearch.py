#Linear Search on Unsorted list
def linear_search(L,e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True

    return found
print(linear_search([19,2,35,4,56,6],6))

#Linear Search on Sorted List
def linear_Search(L,e):
    for i in range(len(L)):
        if L[i]==e:
            return True
        if L[i]>e:
            return False
    return False
print(linear_Search([1,2,3,4,5,6,7,8],8))