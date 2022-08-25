# Python program to identify the identifier

# import re module

# re module provides support
# for regular expressions
import re

# Make a regular expression
# for identify valid identifier
regex = '^[foo][_a-z\dA-Z]*$'
	
# Define a function for
# identifying valid identifier
def check(string):

	# pass the regular expression
	# and the string in search() method
	if(re.search(regex, string)):
		print("Valid Identifier")
		
	else:
		print("Invalid Identifier")
	

# Driver Code
if __name__ == '__main__' :
	
	# Enter the string
	string = "gfg"
	
	# calling run function
	check(string)

	string = "123"
	check(string)

	string = "#abc"
	check(string)
