import datetime
class Person(object):
    def __init__(self,name):
        """Create a person called name"""
        self.name=name
        self.birthday= None
        self.lastName = name.split(' ')[-1]
    def getLastName(self):
        """return self's last name"""
        return self.lastName
    def __str__(self):
        """return self's name"""
        return self.name
    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday= datetime.date(year,month,day)
    def getAge(self):
        """returns self's current age in days"""
        if self.birthday==None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days
    def __lt__(self,other):
        """return True if self's name is lexicographically less than other's name, and false otherwise""" 
        if self.name==other.name:
            return self.Lastname<other.Lastname
        return self.name<other.name       
class MITPerson(Person):
    nextidnum=0
    def __init__(self,name):
        Person.__init__(self,name)
        self.idnum=MITPerson.nextidnum
        MITPerson.nextidnum+=1
    def getIDnum(self):
        return self.idnum
    def __lt__(self,other):
        return self.idnum<other.idnum
    def speak(self,utterance):
        return (self.getLastName()+" says: "+utterance)
class Student(MITPerson):
    pass
class Professor(MITPerson):
    def __init__(self, name,department):
        MITPerson.__init__(self,name)
        self.department=department
    def speak(self,utterance):
        newUtterance='In Course '+ self.department+' we say '
        return MITPerson.speak(self,newUtterance+ utterance)
    def lecture(self,topic):
        return self.speak('it is obvious that'+ topic)
class UG(Student):
    def __init__(self, name,classYear):
        MITPerson.__init__(self,name)
        self.year=classYear
    def getClass(self):
        return self.year
    def speak(self,utterance):
        return MITPerson.speak(self,"Dude, "+utterance)
class Grad(Student):
    pass
class TransferStudent(Student):
    pass
class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students=[]
        self.grades={}
        self.isSorted=True
    def addStudent(self,student):
        """Assumes: student is of type Student
        Add student to grade book"""
        if student in self.students:
            raise ValueError('Duplicate student ')
        self.students.append(student)
        self.grades[student.getIDnum()]=[]
        self.isSorted = False
    def addGrade(self,student,grade):
        """Assumes: grade is a float.
        Add grade to the list of grades for students"""
        try:
            self.grades[student.getIDnum()].append(grade)
        except:
            raise ValueError
    def getGrades(self,student):
        """Return a list of grades for students"""
        try:
            return self.grades[student.getIDnum()][:]
        except KeyError:
            raise ValueError('Student not found')
    def allStudents(self):
        """Return a list of the students in the grade book"""    
        if not self.isSorted:
            self.students.sort()
            self.isSorted= True
        for s in self.students:
            yield s
def gradeReport(course):
        """Assumes : Course is of type grades"""
        report =[]
        for s in course.allStudents():
            tot =0.0
            numGrades=0
            for g in course.getGrades(s):
                tot+=g
                numGrades+=1
                try:
                    average=tot/numGrades
                    report.append(str(s)+'\'s mean grade is'+str(average))
                except ZeroDivisionError:
                    report.append(str(s)+'has no grades')
        return '\n'.join(report)
def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)
    



p1=Person('Elliot Alderson')
p1.setBirthday(1,5,84)
p2=Person('Darlene Alderson')
p2.setBirthday(3,4,86)
p3=Person('Bill Gates')
p3.setBirthday(12,10,55)
p4=Person('Andrew Garfield')
p5=Person('Steve Wozniak')
personList=[p1,p2,p3,p4,p5]
print(p1,"\n")
for i in personList:
    print(i)
print()
personList.sort()
for i in personList:
    print(i)
print()
m3=MITPerson('Eric Grimson')
Person.setBirthday(m3,5,14,84)
m2=MITPerson('Drew Houston')
Person.setBirthday(m2,3,4,83)
m1=MITPerson('Bill Gates')
Person.setBirthday(m1,10,28,55)
MITPersonList=[m1,m2,m3]
for i in MITPersonList:
    print(i)
print(m1.speak("Hi there!"))
MITPersonList.sort()
for i in MITPersonList:
    print(i)
s1=UG('Matt Damon',2017)
s2=UG('Ben Affleck',2017)
s3=UG('Lin Manuel Miranda',2018)
s4=Grad("Leonardo Di Caprio")
s5=TransferStudent('Robert de Niro')
print(s1)
print(s1.getClass())
print(s1.speak('where is the quiz?\n'))
print(s2.speak('I have no clue.\n'))
studentlist=[s1,s2,s3,s4,s5]
studentlist.sort()
for i in studentlist:
    print(i)

faculty=Professor('Doctor Arrogant','six')
print(faculty.speak('Hi there'))
print(faculty.lecture('Hi there'))
ug1= UG('Matt Damon',2018)
ug2=UG('Ben Affleck',2019)
ug3=UG('Drew Houston',2017)
ug4=UG('Mark Zuckerberg',2017)
g1= Grad('Bill Gates')
g2=Grad('Steve Wozniak')
six00=Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)
six00.addGrade(g1,100)
six00.addGrade(g2,25)
six00.addGrade(ug1,95)
six00.addGrade(ug2,85)
six00.addGrade(ug3,75)
print(gradeReport(six00))
six00.addGrade(g1,90)
six00.addGrade(g2,45)
six00.addGrade(ug1,80)
six00.addGrade(ug2,75)
print()
print(gradeReport(six00))