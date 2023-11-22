def genFib():
    fibn_1=1
    fibn_2=0
    while True:
        next = fibn_1+fibn_2
        yield next
        fibn_2=fibn_1
        fibn_1=next
fib=genFib()
print(fib)
for i in range(6):
    print(fib.__next__())   
