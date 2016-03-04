# 2/29/16

number = raw_input("What number should I double? ")

converted = False

while not converted: # not converted, not false, which is True
	try: 														
		number = float(number)									
	except ValueError: 											
		number = raw_input("Sorry that's not a number. Try again. ")
	else: 
		converted = True 

# goes to this when you convert to float successfully 
print("Double that is {}. ".format(number * 2) 

