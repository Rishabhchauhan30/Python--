''''x=float(input('Enter the marks of maths:'))

y=float(input('Enter the marks of physics:'))

z=float(input('Enter the marks of chemistry:'))

if x>=35 and y>=35 and z>=35:
    print('student is pass')
else:
    average=(x+y+z)/3
    print(average)   

phy,chem,maths=[int(x) for x in input("Enter three integer number separated by space").split()]

average=(phy+chem+maths)/3

if phy>=35 and chem>=35 and maths>=35:  #using if else loop for pass/fail determination

    print("The student has passed the exam")

    if average<=59: print("Student has Grade C") #using nested if elif else loop for grading

    elif average<=69: print("Student has Grade B")

    else: print("Student has Grade A")

else: print("The student has failed")'''








