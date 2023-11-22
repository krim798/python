# def oddTuples(aTup):
#     '''
#     aTup: a tuple
    
#     returns: tuple, every other element of aTup. 
#     '''
#     # Your Code Here
#     return (aTup[::2])
#print(oddTuples((1,2,3,4,5,6,7,8,9)))
def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup in reverse order.
    '''
    tuple=()
    index=0
    while index<len(aTup):
        tuple+=(aTup[index],)
        index+=2
    return tuple
print(oddTuples((1,2 ,3,4,5,6,7)))