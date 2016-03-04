# 2/29/16

number = raw_input("What number should I double? ")

try: 														# tries the command (no knowing if it is proper format (int, float, str) 
	number = float(number)									# this must be a float because if not, user enters decimal and it will crash
	print("Double that is {}. ".format(number * 2))			# this must be in try loop or else it wil always to print that 
	# try block only for exception cases 
except ValueError: 											# allows for exception (ValueError is a class, starts with capitals
	print("Sorry that's not a number. ")					# prints this if the input is not a number  


# if the print statement is here, it will print "cheesecheese" 