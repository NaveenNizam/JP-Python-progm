import re

pattern = '^C_[A-Z]+$'

def checkKey(dict, key):  #if given key is present, it will be shown here
    if (re.match(pattern, key)):
        if key in dict.keys():
            print(key, '=', dict[key])
        
        else:   #if given key is not present, 
            print('This Constant is not present')
            y_n = (input(str('Do you want make Constant? ')))  #if given key is present, it will be asked
            if (y_n == 'y' or y_n == 'Yes' or y_n == "YES" or y_n == 'Y' or y_n == 'yes'):
                string = input(str("Constant Value:  "))
                dict.update({key: string})
                print(dict)
            
                
                for i in range(3): #if we want to make more Constant , it will be ask 3 times
                    
                    YesNo = (input(str('Do you want make Constant? ')))

                    if (YesNo == 'y' or YesNo == 'Yes' or YesNo == "YES" or YesNo == 'Y' or YesNo == 'yes'):
                        key = input(str("Constant Key : "))
                        if (re.match(pattern, key)):
                            if key in dict.keys():
                                print( key," It is already declare")
                            else:
                                String = input(str("Constant Value:  "))
                                dict.update({key: String})
                                print(dict)
                        else:
                            print("INVALID CONSTANT")
                    else:
                        print("Have a Nice day")
                        break

            else:
                print("end")
            

    else:
        print("Invalid Constant")


# Driver Code
dict = {
    "C_PI": 3.142,
    "C_GRAVITY": 9.8,
    "C_FACULTY": 'ComputerScience',
    "C_TEACHER": "Ma'm  Madiha",
    "C_SUBJECT": "Compiler Construction",
    "C_DEPARTMENT": 'UBIT',
    "C_GROUPMEMBER": ['Farhia', 'Kinza', 'Lubna', 'Maryam', 'Naveen', 'Sehrish']
}

key = input(
    str("Input Constant , star with 'C_' end with 'any name' in capital letter: "))

checkKey(dict, key)