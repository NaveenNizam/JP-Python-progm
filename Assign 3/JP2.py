"""import math
r = float (input('enter circle radius: '))
r = math.pi *  math.pow (r,2)
print( "The Area of Circle is   ", round(r,2))

a = float (input ('enter a number :   '))
b = float (input ('enter a number :   '))
c = a+b
print("the sum of {0} and {1} is ".format(a,b), round(c,3) ) """

e=float(input("Enter your Math's number:  "))
f=float(input("Enter your Physics number:  "))
g=float(input("Enter your Computer number:  "))
h=float(input("Enter your Chemistry number:  "))
i=float(input("Enter your English number:  "))
j=float(input("Enter your Urdu number:  "))
k=float(input("Enter your Islamiat number:  "))
print('\033[1m' +'Each Subject marks out of 100 \n Passing Marks in each subject is 33' + '\033[0m')
print('\033[1m' + 'TOTAL MARKS IS 700' + '\033[0m')
l = sum ([e,f,g,h,i,j,k])
print('Obtain marks :  ',l)
if e <33:
    print("Uncleared in Math's")
if f < 33:
     print("Uncleared in Physics")
if g< 33:
     print("Uncleared in Computer")
if h < 33:
     print("Uncleared in Chemistry")
if i < 33:
     print("Uncleared in English")
if j < 33:
     print("Uncleared in Urdu")
if k < 33:
     print("Uncleared in Islamiat")
m = (l/ 700 )*100
print ('Percentage is   ',round(m,3))
if m >= 80:
    print ('your grade is A+')
elif m < 80 and m >=70:
    print('your grade is A')
elif m < 70 and m >=60:
    print('your grade is B')
elif m < 60 and m >=50:
     print('your grade is C')
elif m < 50 and m >=40:
    print('your grade is D')
elif m < 40 and m ==35:
    print('your grade is E')
else :
    print ("FAIL!")   



