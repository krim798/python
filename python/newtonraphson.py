#newton-raphson
epsilion=0.01
y=int(input("Enter number:"))
guess=y/2.0
numGuesses=0
while abs(guess*guess-y)>=epsilion:
    numGuesses+=1
    guess=guess-(((guess**2)-y)/(2*guess))
print('numGuesses='+str(numGuesses))
print('Square root of'+str(y)+'is about'+str(guess))