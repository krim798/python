# #fn
# #def g(x):
#   #      x='abc'
#    # x+=1
#     #print('in g(x): x = ',x)
#     #h()
#     #return x
# #x=3
# #z=g(x)
# '''
# def a(x, y, z):
#      if x:
#          return y
#      else:
#          return z

# def b(q, r):
#     return a(q>r, q, r)
# print(b(a,b))
# '''
# """
# a= 10
# def f(x):
#     return x+a
# a=3 
# print(f(1))
# """
# '''
# def foo(x, y = 5):
#    def bar(x):
#       return x + 1
#    return bar(y * 2)
          
# print(foo(3,0))
# '''
# '''
# def fourthPower(x): 

#     x: int or float.

#     # Your code here
#     return x**4
# x=int(input("Enter number:"))
# print(fourthPower(x))
# '''

# '''def get_sum_metrics(predictions, metrics=[]):
#     x=0
#     for i in range(3):
#         metrics.append(lambda x: x + i)

#     sum_metrics = 0
#     for metric in metrics:
#         sum_metrics += metric(predictions)

#     return sum_metrics
# '''
# '''def fact(a):
#     if a==0:
#         return 1
#     else:
#         return a*fact(a-1)
# print(fact(0))'''
# '''def iterPower(base, exp):
    
#     base: int or float.
#     exp: int >= 0
 
#     returns: int or float, base^exp
#         # Your code here
#     expo=1
#     if exp==0:
#        return 1
#     else:
#        for i in range(1,exp+1):
#          expo*=base
#        return expo
# print(iterPower(2,4))'''
# '''for i in range(2):
#     name=input("name")
#     nameHandle.write(name+'\n')
# nameHandle.close()'''
# # x=(1,(2,'John',4),'Hi')
# # print(x[0:-1])                     
# # def oddTuples(aTup):
# #     '''
# #     aTup: a tuple
    
# #     returns: tuple, every other element of aTup. 
# #     '''
# #     # Your Code Here
# #     return (aTup[::2])
# # print(oddTuples((1,2,3,4,5,6,7,8,9)))
# # x = [9,6,0,3]
# # z=x.sort
# # print(z)
# # k=x.insert(0,100)
# # x.remove(3)
# # x.append(7)
# # y=x.extend([1,2,3,5])
# # print(x)
# # print(x.pop())
# # print(x)
# # aList = [0, 1, 2, 3, 4, 5]
# # bList = aList
# # aList[2] = 'hello'
# # print(aList is bList)
# # y=map(int,[1,-2,3.6,-4.5])
# # for i in y:
# #     print(i)
# # def applyToEach(L, f):
# #     for i in range(len(L)):
# #         L[i] = f(L[i])
# #     return L
# # testList=[1,-4,8,-9]
# # def absolute(b):
# #      return b+1
# # print(applyToEach(testList,absolute))
# # def applyEachTo(L, x):
# #     result = []
# #     for i in range(len(L)):
# #         result.append(L[i](x))
# #     return result
# # def square(a):
# #     return a*a

# # def halve(a):
# #     return a/2

# # def inc(a):
# #     return a+1
# # print(applyEachTo([inc, square, halve, abs], 3.0))
# # import numpy as np
# # def randomization(n):
# #     """
# #     Arg:
# #       n - an integer
# #     Returns:
# #       A - a randomly-generated nx1 Numpy array.
# #     """
# #     #Your code here
# #     n=int(input("Enter n:"))
# #     A=np.random.random([n,1])
# #     print("A =", A)
# #     return None
# # randomization()
# x=[1,2,3]
# x=x+[3,4,5,6]
# print(x)
# x.append((2,3,4))
# print(x)
# x.extend([1,2,3])
# print(x)
# del(x[1])
# print(x)
# for i in x:
#     x.pop()
# print(x)
# #  x[2]=4
# #  print(x) 
# #  x=4
# # y=5
# # x,y=y,x
# # print('x=',x,'\ty=',y)
# # def quotient_and_remainder(x, y):
# #          q = x//y
# #          r = x%y
# #          return (q, r)
# # print(quotient_and_remainder(4,5))
# s='abcdefghijklmnopqrstuvwxyz'
# y=list(s)
# print(y)
# print(' '.join(y))
# y=range(2,6)
# print(y)
# z=['red','green','violet','orange','yellow']
# sort= sorted(z)
# print(sort)
# print(z)
# sortedz=z.sort()
# print(z)
# animals = {'a': 'aardvark', 'b': 'baboon', 'c': ['coati','dd','dddd']}
# animals['d'] = 'donkey'
# print(animals)
# def how_many(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.

#     returns: int, how many values are in the dictionary.
#     '''
#     # Your Code Here
#     for i in range(len(aDict.values())):
#         i+=1
#     return i
# print(how_many(animals))


# 
#print(int('1')/2.0)


# while True:
#     try:
#         a=input("a:")
#         a=int(a)
#         break
#     except ValueError:
#         print("input not an int")
# print('correct')
# data=[]
# f='C:\Users\hp\Desktop\9\python\python\words.txt'
# fh=open(f,'r')
# try:
#     fh=open(f,'r')
# except IOError:
#     print("Cannot open file",f)
# else:
#     for new in fh:
#         if new!='\n':
#             addit=new[:-1].split(' ')
#             data.append(addit)
#     fh.close()
# def fancy_divide(numbers,index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError:
#         print("-1")
#     else:
#         print("1")
#     finally:
#         print("0")
# print(fancy_divide([0, 2, 4], 0))

# def fancy_divide(list_of_numbers, index):
#     try:
#         try:
#             raise Exception("0")
#         finally:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#     except Exception as ex:
#         print(ex)


# def fancy_divide(list_of_numbers, index):
#     try:
#         try:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#         finally:
#             raise Exception("0")
#     except Exception as ex:
#         print(ex)
# print(fancy_divide([0, 2, 4], 0))


# def fancy_divide(list_of_numbers, index):
#    denom = list_of_numbers[index]
#    return [simple_divide(item, denom) for item in list_of_numbers]
# def simple_divide(item,denom):
#      try:
#        return item/denom
#      except ZeroDivisionError:
#        return 0
#      except:
#        raise Exception
# print(fancy_divide([0,2,4],6))


# class Clock(object):
#   def __init__(self, time):
#     self.time = time
#   def print_time(self):
#       print(self.time)
# clock = Clock('5:30')
# clock.print_time('10:30')



# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         print(self.time)

# boston_clock = Clock('5:30')
# paris_clock = boston_clock
# paris_clock.time = '10:30'
# boston_clock.print_time()


# class Wild(object):
#     def __init__(self, x, y): 
#         self.y = y
#         self.x = x
#     def getX(self):
#         return self.x 
#     def getY(self):
#         return self.y

# X = 7
# Y = 8
# wild = Wild(17,18)
# print(wild.getX())
# wild2=Wild(X,18)
# print(wild2.getX())


# class po(object):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
    #     return self.x

    # def getY(self):
    #     # Getter method for a Coordinate object's y coordinate
    #     return self.y

    # def __str__(self):
    #     return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    # def __eq__(self,other):
    #     assert type(self)==type(other)
    #     return self.getX()==other.getX() and self.getY()==self.getY()
    # def __repr__(self):
    #     return "po("+str(self.getX())+","+str(self.getY())+")"
# import numpy as np
# print(np.random.random([4,3]))

# def prime_generator():
#     yield 2
#     primes = [2]
#     number = 3
#     while True:
#         for prime in primes:
#             if number % prime == 0:
#                 break
#         else:
#             primes.append(number)
#             yield number
#         number += 2

# def print_prime_numbers(n):
#     generator = prime_generator()
#     for _ in range(n):
#         print(next(generator))

# print_prime_numbers(10)


def program1(x):
    total = 0
    for i in range(1000):
        total += i

    while x > 0:
        x -= 1
        total += x

    return total
print(program1(0))

import math

class Calculator:
    def __init__(self):
        self.variables = {}

    def calculate(self, equation):
        try:
            return eval(equation, self.variables, math.__dict__)
        except Exception as e:
            return str(e)

    def set_variable(self, variable, value):
        self.variables[variable] = value

calculator = Calculator()
while True:
    print("\nEnter an equation or command. Type 'help' for a list of commands.")
    print("For example: 3+5, sin(pi/2), set a 5, a+b, variables")
    print("Type 'exit' to exit the program.")
    user_input = input(">>> ")
    if user_input.lower() == 'exit':
        break
    elif user_input.lower() == 'help':
        print("\nList of commands:")
        print("set variable value")
        print("variables (to see a list of defined variables)")
        print("clear (to clear the calculator)")
        print("exit (to exit the program)")
    elif user_input.lower().startswith('set '):
        variable, value = user_input.lower().split(' ')
        calculator.set_variable(variable, float(value))
    elif user_input.lower() == 'variables':
        print("List of variables:")
        for variable, value in calculator.variables.items():
            print(f"{variable}: {value}")
    elif user_input.lower() == 'clear':
        calculator.variables.clear()
    else:
        print("Result: ", calculator.calculate(user_input))                                                                                                 