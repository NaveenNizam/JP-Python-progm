'''print ('Twinkle, twinkle, little star, \n \t How I wonder what you are! \n \t \t Up above the world so high, \n \t \t Like a diamond in the sky \n Twinkle, twinkle,little star, \n \t How i wonder what you are '
)
import sys      # 'SYS' -> System-specific parameters and functions
print('\033[1m' + ' \t \t*****PYTHON VERSION*****' + '\033[0m') #\033 is octal and used to text bold
print(sys.version)                                              # 0m after the string the reset formatting for any following strings.
print('\033[1m' + ' \t \t******VERSION INFO******' + '\033[0m') # 1m before a string to print the string in bold
print (sys.version_info)     #sys module provides information 
                                 #about constants, functions and methods of the Python interpreter. 
import datetime
a = datetime.datetime.now()
#print ('\n \nDate time is ',a)    %d ->date %a -> day also %B ->month name
b = a.strftime("\n Date:  %d-%m-%Y  \n Day: %a \n time: %H:%M:%S") #strf --> string formatter,this will format a datetime object to string format.
print("Current date and time ", b) '''

name = (input('Enter your full name: '))
reverse = name[::-1]
print(reverse)