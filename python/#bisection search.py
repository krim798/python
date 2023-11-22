#bisection search
print("Please think of a number between 0 and 100!")
x=100
eps=0.01
low=0
high=x
ans=(high+low)//2
while abs(ans**2-x)>=eps:
        print("Is your secret number",int(ans),'?')
        y=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if y=='h':
            high=ans
        elif y=='l':
            low=ans
        elif y=='c':
             print("Game over. Your secret number was:",int(ans))
             break
        else:
             print("Sorry, I did not understand your input.")
        ans=(high+low)//2