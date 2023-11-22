#to check whether a char is in a string using recursion
def isIn(char,aStr):
    if len(aStr)==0:
        return False
    if len(aStr)==1:
        return aStr==char
    midIndex=len(aStr)//2
    midChar=aStr[midIndex]
    if midChar == char :
        return True
    elif char<midChar:
        return isIn(char,aStr[:midIndex])
    else:
        return isIn(char,aStr[midIndex+1:])
x=input("Enter character:")
y=input("Enter a string:")
print (isIn(x, y))
