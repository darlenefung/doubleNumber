# 2/29/16

number = raw_input("What number should I double? ")

while number != "no": 
	try: 														
		number = float(number)									
		print("Double that is {}. ".format(number * 2))			 
	except ValueError: 											
		raw_input("Sorry that's not a number. Try again or type 'no' to quit. ")
	else: 
		print("Have a nice day!")
		exit()

