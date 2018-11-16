import math

while True:
	menu = '''
	Choose the math operation.
	
	0 - Addition
	1 - Subtraction
	2 - Multiplication
	3 - Division
	4 - Modulo
	5 - Raising to a Power
	6 - Square Root 
	7 - Logarithm
	8 - Sine
	9 - Cosine
	10 - Tangent
	'''
	print(menu)
	
	oper = input("\tYour option from the menu: ")
	
	#Addition
	if oper == "0":
		val1 = float(input("First value: "))
		val2 = float(input("Second value: "))
		
		print(f"The results is: {val1 + val2}\n")
		
		back = input("Go back to main menu? (y/n) ")
		
		#Going back to main menu or exiting the program
		if back == 'y':
			continue
		else:
			break
			
			
	#Subtraction
	elif oper == "1":
		val1 = float(input("First value: "))
		val2 = float(input("Second value: "))
		
		print(f"The results is: {val1 - val2}\n")
		
		back = input("Go back to main menu? (y/n) ")
		
		#Going back to main menu or exiting the program
		if back == 'y':
			continue
		else:
			break
			
			
	#Multiplication
	elif oper == "2":
		val1 = float(input("First value: "))
		val2 = float(input("Second value: "))
		
		print(f"The results is: {val1 * val2}\n")
		
		back = input("Go back to main menu? (y/n) ")
		
		#Going back to main menu or exiting the program
		if back == 'y':
			continue
		else:
			break
			
			
	#Division
	elif oper == "3":
		val1 = float(input("First value: "))
		val2 = float(input("Second value: "))
		
		print(f"The results is: {val1 / val2}\n")
		
		back = input("Go back to main menu? (y/n) ")
		
		#Going back to main menu or exiting the program
		if back == 'y':
			continue
		else:
			break
			
			
	#Modulo
	elif oper == "4":
		val1 = float(input("First value: "))
		val2 = float(input("Second value: "))
		
		print(f"The results is: {val1 % val2}\n")
		
		back = input("Go back to main menu? (y/n) ")
		
		#Going back to main menu or exiting the program
		if back == 'y':
			continue
		else:
			break
			
			
	#Raise to the Power
	elif oper == "5":
		val1 = float(input("First value: "))
		val2 = float(input("Second value: "))
		
		print(f"The results is: {math.pow(val1, val2)}\n")
		
		back = input("Go back to main menu? (y/n) ")
		
		#Going back to main menu or exiting the program
		if back == 'y':
			continue
		else:
			break
			
			
	#Square Root
	elif oper == "6":
		val1 = float(input("First value: "))
		
		print(f"The results is: {math.sqrt(val1)}\n")
		
		back = input("Go back to main menu? (y/n) ")
		
		#Going back to main menu or exiting the program
		if back == 'y':
			continue
		else:
			break
			
			
	#Logarithm
	elif oper == "7":
		val1 = float(input("First value: "))
		
		print(f"The results is: {math.log(val1, 2)}\n")
		
		back = input("Go back to main menu? (y/n) ")
		
		#Going back to main menu or exiting the program
		if back == 'y':
			continue
		else:
			break
			
			
	#Sine
	elif oper == "8":
		val1 = float(input("First value: "))
		
		print(f"The results is: {math.sin(math.radians(val1))}\n")
		
		back = input("Go back to main menu? (y/n) ")
		
		#Going back to main menu or exiting the program
		if back == 'y':
			continue
		else:
			break
			
			
	#Cosine
	elif oper == "9":
		val1 = float(input("First value: "))
		
		print(f"The results is: {math.cos(math.radians(val1))}\n")
		
		back = input("Go back to main menu? (y/n) ")
		
		#Going back to main menu or exiting the program
		if back == 'y':
			continue
		else:
			break
			
			
	#Tangent
	elif oper == "10":
		val1 = float(input("First value: "))
		
		print(f"The results is: {math.tan(math.radians(val1))}\n")
		
		back = input("Go back to main menu? (y/n) ")
		
		#Going back to main menu or exiting the program
		if back == 'y':
			continue
		else:
			break
			
	#Handling invalid options		
	else:
		print("Invalid Option")
		continue
		
		
			
			