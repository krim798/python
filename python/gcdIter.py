def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a%b==0:
        return b
    elif b%a==0:
        return a
    if a<b:
       for i in range(a,1,-1):
            if a%i==0 and b%i==0:
                return i
    else:
        for i in range(b,1,-1):
            if a%i==0 and b%i==0:
                return i
x=int(input("x"))
y=int(input("y"))
print(gcdIter(x, y))