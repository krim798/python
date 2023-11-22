#fibonacci using dictionary
def fibonacci_effective(n,d):
    global numfunccall
    numfunccall+=1   
    if n in d:
        return d[n]
    else:
        ans=fibonacci_effective(n-1,d) + fibonacci_effective(n-2,d)
        d[n]=ans
    return ans
d={1:1,2:2}
numfunccall=0
print(fibonacci_effective(190,d),numfunccall)