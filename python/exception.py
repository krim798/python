#try and except
try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(a/b)
    print("Okay")
except ValueError:
    print("Can't convert to a number")
except ZeroDivisionError:
    print ("You can't divide by zero!")
except:
    print('Bug detected')
print("outside")
 
