# =============================================================================
# This code follows the tutorials by Paul McWhorter (TopTechBoy.com).
# I wrote this to practice Python syntax and VPython 3D library.
# =============================================================================

import time
from time import sleep
from threading import Thread
import pickle

# =============================================================================
# Python Basic Tutorials (1-20)
# =============================================================================

def Python_Tutorial_1():
    print('Hello World')
    radius = 5
    area = 3.14*radius**2
    print ('A circle of radius',radius,'has an area of',area)

def Python_Tutorial_2():
    picture = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print (picture[1])
    print (picture[1][2])
    x = []
    x.append(50)
    print(x)
    x.append(60)
    print(x)
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    grads=[a,b,c,d,e]
    print(grads)

def Python_Tutorial_3():
    x = 7
    y = 2
    z = x+y
    print(x,'+',y,'=',z)
    try:
        num = input('Please Input Your Number: ')
        print('Your Number is ',num)
        name = input('Please Enter Your Name: ')
        print('Hello',name,', Welcome to Python')
    except: pass

def Python_Tutorial_4():
    try:
        num1 = float(input('Please Enter Your First Number: '))
        num2 = float(input('Please Enter Your Second Number: '))
        an = num1 + num2
        print (num1,' + ',num2,' = ',an)
    except: pass

def Python_Tutorial_5():
    # Install Visual Studo Code.
    print("Install Visual Studio Code.")

def Python_Tutorial_6():
    try:
        mynumber = float(input('Please Input Your Number: '))
        rem = mynumber%2
        if (rem==0):
            print('You have an Even Number')
            print('Please Play Again!')
        if (rem==1):
            print('You have an Odd Number')
            print('Please Play Again!')
    except: pass

def Python_Tutorial_7():
    try:
        mynum = float(input('Please Input Your Number: '))
        if (mynum>=5 and mynum<=10):
            print('Congratulations, Your Number is Between 5 and 10')
        if (mynum<5 or mynum>10):
            print('Sorry,Your Number is Not between 5 and 10')
    except: pass

def Python_Tutorial_8():
    try:
        mynum = float(input('Please Input Your Number: '))
        rem = mynum%2
        if (mynum>0 and rem==0):
            print ('You Have an Even Positive Number')
        if (mynum>0 and rem== 1):
            print ('You Have an Odd Positive Number')
        if (mynum<0 and rem==0):
            print ('You Have an Even Negative Number')
        if (mynum<0 and rem==1):
            print ('You Have an Odd Negative Number')
        if (mynum==0):
            print('Your Number is Zero')
    except: pass

def Python_Tutorial_9():
    try:
        numgrades = int (input('How Many Grades Do You Have? '))
        grades = []
        for i in range(0,numgrades,1):
            grade = float(input('Please Enter Your Grade: '))
            grades.append(grade)
            print(grades)
        print('Your Grades Are: ')
        for i in range(0,numgrades,1):
            print(grades[i])
        print('That All folks')
    except: pass

def Python_Tutorial_10():
    try:
        numgrades = int (input('How Many Grades Do You Have? '))
        grades = []
        Grades = 0.0
        for i in range(0,numgrades,1):
            grade = float(input('Please Enter Your Grade: '))
            grades.append(grade)
            print(grades)
        print('Your Grades Are: ')
        for i in range(0,numgrades,1):
            print(grades[i])
        for a in range(0,numgrades,1):
            Grades = Grades + grades[a]
        Average = Grades/numgrades
        print('')
        print ('Your Average is: ',Average)
    except: pass

def Python_Tutorial_11():
    try:
        numgrades = int (input('How Many Grades Do You Have? '))
        grades = []
        Grades = 0.0
        lowGrade = 100
        highGrade = 0
        for i in range(0,numgrades,1):
            grade = float(input('Please Enter Your Grade: '))
            grades.append(grade)
            print(grades)
        print('Your Grades Are: ')
        for i in range(0,numgrades,1):
            print(grades[i])
        for a in range(0,numgrades,1):
            Grades = Grades + grades[a]
        Average = Grades/numgrades
        print('')
        print('Your Average is: ',Average)
        for i in range(0,numgrades,1):
            if grades[i]<lowGrade:
                lowGrade = grades[i]
        print('Your Low Grade is: ',lowGrade)
        for  i in range(0,numgrades,1):
            if grades[i]>highGrade:
                highGrade = grades[i]
        print('Your High Grade is: ',highGrade)
    except: pass

def Python_Tutorial_12():
    try:
        numgrades = int(input('How Many Grades Do You Have? '))
        grades = []
        Grades = 0.0
        lowGrade = 100
        highGrade = 0
        for i in range(0,numgrades,1):
            grade = float(input('Please Enter Your Grade: '))
            grades.append(grade)
            print(grades)
        print('Your Grades Are: ')
        for i in range(0,numgrades,1):
            print(grades[i])
        for a in range(0,numgrades,1):
            Grades = Grades + grades[a]
        Average = Grades/numgrades
        print('')
        print('Your Average is: ',Average)
        for i in range(0,numgrades,1):
            if grades[i]<lowGrade:
                lowGrade = grades[i]
        print('Your Low Grade is: ',lowGrade)
        for  i in range(0,numgrades,1):
            if grades[i]>highGrade:
                highGrade = grades[i]
        print('Your High Grade is: ',highGrade)
        for i in range(0,numgrades-1,1):
            for i in range(0,numgrades-1,1):
               if grades[i]<grades[i+1]:
                   swp=grades[i]
                   grades[i]=grades[i+1]
                   grades[i+1]=swp
        print ('Your Sorted Grade List is: ')
        for i in range(0,numgrades,1):
            print(grades[i])
    except: pass

def Python_Tutorial_13():
    try:
        numgrades = int (input('How Many Grades Do You Have? '))
        j = 1
        i = 0
        grades = []
        while(j<=numgrades):
            grade = float(input('Please Enter Your Grade: '))
            grades.append(grade)
            print(grades)
            j=j+1
        while(i<numgrades):
            print(grades[i])
            i = i+1
    except: pass

def Python_Tutorial_14():
    fruits = ['apples','oranges','bananas']
    x = 7
    y = 3.14
    nuts = ['pecans','almond']
    grades = [99,100,56,77,85]
    dataSet = [fruits,x,y,nuts,grades]
    try:
        with open('myData.pk1','wb') as f:
            pickle.dump(dataSet,f)
        with open('myData.pk1','rb') as f2:
            bigKahuna = pickle.load(f2)
        for dt in bigKahuna:
            print(dt)
    except Exception as e:
        print("File Error:", e)

def Python_Tutorial_15():
    try:
        names = []
        grades = []
        grade = []
        numStudents = int(input('How Many Students Do You Have? '))
        for j in range(0,numStudents,1):
            name = input('Plese Enter Student Name: ')
            names.append(name)
            prompt = 'Please Enter '+name+"'s grade "
            grade = float(input(prompt))
            grades.append(grade)
        with open('studentData.pk1','wb')as dataF:
            pickle.dump(numStudents,dataF)
            pickle.dump(names,dataF)
            pickle.dump(grades,dataF)
        with open('studentData.pk1','rb')as readF:
            numStudents = pickle.load(readF)
            numes = pickle.load(readF)
            grades = pickle.load(readF)
        while True:
            name = input('Which Student Do You Want To Check? (Type "exit" to quit) ')
            if name == 'exit': break
            found = False
            for i in range(0,numStudents,1):
                if (names[i] == name):
                    print(str(name),"'s grade is "+str(grades[i])+'.')
                    found = True
            if not found:
                print("Student not found.")
    except: pass

def Python_Tutorial_16():
    try:
        def numgrades(num):
            num = int(input('How Many Grade Do Your Have: '))
            return num
        def grade(nums):
            grades = []
            for i in range(0,nums,1):
                grade = float(input('Please Enter Your Grade: '))
                grades.append(grade)
            return grades
        def Average(nums,grades):
            Grades = 0.0
            for i in range(0,nums,1):
                Grades = Grades+grades[i]
            average = Grades/nums
            return average
        def lowgrade(grades):
            lowGrade = 100
            for i in range(0,len(grades)):
                if grades[i]<lowGrade:
                    lowGrade = grades[i]
            return lowGrade
        def highgrade(grades):
            highGrade = 0
            for i in range(0,len(grades)):
                if grades[i]>highGrade:
                    highGrade = grades[i]
            return highGrade

        num = []
        nums = numgrades(num)
        print(nums)
        grades = grade(nums)
        print(grades)
        average = Average(nums,grades)
        print('Your Average = ',average)
        lowGrade = lowgrade(grades)
        print('Your lowgrade = ',lowGrade)
        highGrade = highgrade(grades)
        print('Your highgrade = ',highGrade)
    except: pass

def Python_Tutorial_17():
    try:
        def inputGrades(nm):
            grades = []
            for i in range(0,nm,1):
                grd = float (input('Please Enter Your Grade: '))
                grades.append(grd)
            return grades
        def printGrades(nm,x):
            for i in range(0,nm,1):
                print(x[i])
        def averageGrades(nm,x):
            tot = 0
            for i in range(0,nm,1):
                tot = tot+x[i]
            average = tot/nm
            return average
        def highLow(nm,x):
            highG = 0
            lowG = 100
            for i in range(0,nm,1):
                if (x[i]<lowG):
                    lowG = x[i]
                if (x[i]>highG):
                    highG = x[i]
            return highG,lowG
        numGrades = int(input('How Many Grade? '))
        myGrades = inputGrades(numGrades)
        print('')
        print('Your Grades Are: ')
        printGrades(numGrades,myGrades)
        print('')
        avg = averageGrades(numGrades,myGrades)
        print('Your Average is: ',round(avg,1))
        highG, lowG = highLow(numGrades,myGrades)
        print('Your High Grade Is: ',highG)
        print('Your Low Grades Is: ',lowG)
    except: pass

def Python_Tutorial_18():
    try:
        class Student:
            def __init__(self,n,gn):
                self.name = n
                self.gradesnum = gn
            def askg(self):
                self.gra = []
                for i in range(0,self.gradesnum,1):
                    grad = float(input('Please Enter '+self.name+"'s Grades: "))
                    self.gra.append(grad)
                return(self.gra) 
            def average(self):
                Grades = 0.00
                for i in range(0,self.gradesnum,1):
                    Grades = Grades + self.gra[i]
                average = Grades/self.gradesnum
                return average
            def highg(self):
                highg = 0
                for i in range(0,self.gradesnum,1):
                    if(self.gra[i]>highg):
                        highg = self.gra[i]
                return highg
            def lowg(self):
                lowg = 100
                for i in range(0,self.gradesnum,1):
                    if(self.gra[i]<lowg):
                        lowg = self.gra[i]
                return lowg
        
        name1 = Student('a',3)
        nameg1 = name1.askg()
        print(nameg1)
        
        while True:
            sname = input('Which Student Do You Want To Check? (Type "exit" to quit) ')
            if sname == 'exit': break
            if name1.name == sname:
                print('name:',name1.name)
                print('Average = ',name1.average())
                print('Highgrade = ',name1.highg())
                print('Lowgrade = ',name1.lowg())
    except: pass

def Python_Tutorial_19():
    try:
        class Students:
            def __init__(self,first,last):
                self.first = first
                self.last = last
            def gInput(self,ng):
                self.ng=ng
                self.grades = []
                for i in range(0,self.ng,1):
                    grd = float(input('Please Enter '+self.first+"'s Grade: "))
                    self.grades.append(grd)
                return self.grades
            def printGrades(self):
                print(self.first,self.last,"'s Grades are: ")
                for i in range(0,self.ng,1):
                    print(self.grades[i])
                print('')
            def avGrades(self):
                bucket = 0
                for i in range(0,self.ng,1):
                    bucket = bucket+self.grades[i]
                avg = bucket/self.ng
                return avg
            def highLow(self):
                highGrade = 0
                lowGrade = 100
                for i in range(0,self.ng,1):
                    if self.grades[i]>highGrade:
                        highGrade = self.grades[i]
                    if self.grades[i]<lowGrade:
                        lowGrade = self.grades[i]
                return lowGrade,highGrade
        
        student1 = Students('Joe','Evans')
        student1.gInput(2) 
        student1.printGrades()
        print('Average is: ',student1.avGrades())
    except: pass

def Python_Tutorial_20():
    try:
        def myBox(delayT,color):
            while True:
                print('...My Box is Open')
                sleep(delayT)
                print('...My Box is Closed')
                sleep(delayT)
        def myLED(delayT,color):
            while True:
                print('My LED is On')
                sleep(delayT)
                print('My LED is Off')
                sleep(delayT)
        
        print("Press Ctrl+C to stop threading tutorial.")
        delayBox = 5
        delayLED = 1
        boxThread = Thread(target=myBox, args=(delayBox,'red'))
        LEDThread = Thread(target=myLED, args=(delayLED,'blue'))
        boxThread.daemon=True
        LEDThread.daemon=True
        boxThread.start()
        LEDThread.start()
        
        time.sleep(10)
        print("Tutorial 20 demo finished.")
    except: pass

# =============================================================================
# Homeworks
# =============================================================================

def Python_Tutorial_3_Homework():
    try:
        num1 = input('Please Input Your First Number: ')
        num2 = input('Please Input Your Second Number: ')
        an = num1 + num2
        print (num1,' + ',num2,' = ',an)
    except: pass

def Python_Tutorial_9_Homework():
    try:
        numgrades = int (input('How Many Grades Do You Have? '))
        grades = []
        Grades = 0.0
        for i in range(0,numgrades,1):
            grade = float(input('Please Enter Your Grade: '))
            grades.append(grade)
            print(grades)
        print('Your Grades Are: ')
        
        for i in range(0,numgrades,1):
            print(grades[i])
        for a in range(0,numgrades,1):
            Grades = Grades + grades[a]
        Average = (Grades/numgrades)
        print ('Your Average is: ',Average)
    except: pass
