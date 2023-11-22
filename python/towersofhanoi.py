#towers of hanoi
def printMove(fr,to):
    print("move disk from rod", fr," to ", to)
def Towers(n,fr,to,spare):
    if n==1:
        printMove(fr ,to )
    else:
        Towers (n-1,fr, spare, to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)
print(Towers(4,'P1','P2','P3'))