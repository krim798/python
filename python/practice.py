import random
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
def sum(x,y):
    return x+y
def areaOfTriangle(b,h):
    return str(0.5*b*h)+"sq units"
def swap_2_numbers(x,y):
    x,y=y,x
    print('X=',x,'\tY=',y)
def printList(x=[]):
    for i in range(1,31):
        x.append(i**2)
    return(x[5:])
def fact(x):
    fact =1
    for i in range(1,x+1):
        fact*=i
    return fact
def oddEven(x):
    for i in x:
        if i%2==0:
            print("Even")
        else:
            print("Odd")
def multiplicationTable(x):
    for i in range(1,11):
        print(x,'*',i,'=',x*i)
def maxOf3Num(a,b,c):
    if a>b and a>c:
        print(a," is the max value ")
    elif b>a and b>c:
        print(b,"is the max value")
    else:
        print(c,'is the max value')
    return True
def randomStoryGenerator():
    start=['Once upon a time','In the 20 BC','A long time ago']
    adjective=['happy','sad','angry','afraid']
    noun=['dog','human','cat']
    verb=['works','dances','eats']
    adverb=['enthusiastically','quickly','softly']
    story=print(random.choice(start),'there was a ',random.choice(adjective),' ',random.choice(noun),'. One day, the ',random.choice(noun),random.choice(verb),random.choice(adverb))
    return story
def fakeDatasetGenereation():
    fake=Faker()
    tranDate=[]
    CustName=[]
    CardNum=[]
    zipCode=[]
    transAmount=[]
    for i in range(100):
        tranDate.append(fake.date_time_between_dates("-1y",'now'))
        CustName.append(fake.name())
        CardNum.append(fake.credit_card_number())
        zipCode.append(fake.zipcode())
        transAmount.append(np.random.randint(100,50000))  
    data=pd.DataFrame(zip(tranDate,CustName,CardNum,zipCode,transAmount),columns=["Transaction Date","Customer Name","Card Number","Zip Code","Transaction Amount"])
    x=data.head() 
    y=data.shape
    z=data.to_csv("syntheticBankData.csv")
    return x 
    return z

def additionofarrays(arr1,arr2):
    return np.add(arr1,arr2)
def subtraction(arr1,arr2):
    return np.subtract(arr1,arr2)
def multiply(arr1,arr2):
    return np.multiply(arr1,arr2)
def matrixmul(arr1,arr2):
    return np.matmul(arr1,arr2)
def randomArray():
    return np.random.randint(1,100,size=(3,3))
def maxof(randomArray):
    return np.max(randomArray())
def min(randomArray):
    return np.min(randomArray())
def plot():
    np.random.seed(42)
    data={
        'A':np.random.normal(0,1,100),'B':np.random.normal(3,1.5,100),'C':np.random.normal(-2,0.5,100)
    }
    df=pd.DataFrame(data)
    print("Basic Statistics:")
    print(df.describe())
    plt.figure(figsize=(10,6))
    plt.hist(df['A'],bins=20,alpha=0.5,label='A')
    plt.hist(df['B'],bins=20,alpha=0.5,label='B')
    plt.hist(df['C'],bins=20,alpha=0.5,label='C')
    plt.title('Histogram of data')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
    #box plot
    plt.figure()
    sns.boxplot(data=df)
    plt.title("Box plot of data")
    plt.show()
    #scatter plot
    plt.figure()
    plt.scatter(df['A'],df['B'],label='A vs B')
    plt.scatter(df['A'],df['C'],label='A vs C')
    plt.xlabel('A')
    plt.ylabel('values')
    plt.legend(loc='lower right')
    plt.show()
# plot()
def linearRegression():
    np.random.seed(42)
    x=2*np.random.rand(100,1)
    y=4+3*x+np.random.randn(100,1)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    model=LinearRegression()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    mse=mean_squared_error(y_test,y_pred)
    print("Mean squared error:",mse)
    plt.scatter(x_train,y_train,label='Training data')
    plt.plot(x_test,y_pred,color='red',linewidth=3,label='Linear Regression line')
    plt.title('Linear Regression')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
print(fakeDatasetGenereation())