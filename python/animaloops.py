from typing import Any
import random


class animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age=newage
    def set_name(self,newname=''):
        self.name=newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
class cats(animal):
    def speak(self):
        print("Meow")
    def __str__(self):
        return "Cat:"+str(self.name)+":"+str(self.age)
class rabbits(animal):
    tag=1
    def __init__(self,age,parent1=None,parent2=None):
        animal.__init__(self,age)
        self.parent1=parent1
        self.parent2=parent2
        self.rid=rabbits.tag
        rabbits.tag+=1
    def speak(self):
        print('Meep')
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self,other):
        return rabbits(0,self,other)
    def __eq__(self,other):
        parents_same=self.parent1.rid==other.parent1.rid and self.parent2.rid==other.parent2.rid
        parents_opposite= self.parent2.rid==other.parent1.rid and self.parent1.rid==other.parent2.rid
        return parents_same or parents_opposite    
        
    def __str__(self):
        return "Rabbit:" + str(self.name) + ":" + str(self.age)
class Person(animal):
    def __init__(self,name, age):
        animal.__init__(self,age)
        animal.set_name(self,name)
        self.friends=[]
    def get_friends(self):
        return self.friends
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self,other):
        diff=self.get_age()-other.get_age()
        if self.age>other.age:
            print(self.name,'is',diff,'years older than',other.name)
        else:
            print(self.name,'is',-diff,'years younger than',other.name)
    def __str__(self):
        return "person:"+str(self.name)+':'+str(self.age)
class student(Person):
    def __init__(self,name, age,major=None):
        self.major=major
    def change_major(self,major):
        self.major=major
    def speak(self):
        r=random.random()
        if r<0.25:
            print("I have homework")  
        elif 0.25<=r<0.5:
            print("I need sleep") 
        elif 0.5<=r<0.75:
            print("I should eat")
        else:
            print("I am watcghing tv")
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)     
myanimal=animal(3)
print(myanimal)
myanimal.set_name('foobar')
print(myanimal)
print(myanimal.get_age())
print(myanimal.age)
