menu = """

1. Reverse a string
2. Reverse a sentence
3. Find the minimum value in a list
4. Find the maximum value in a list
5. Calculate the remainder of a given numerator and denominator
6. Return distinct values from a list including duplicates 
7. Return distinct values and their counts
8. Exit menu

""" 

while(True):
	print(menu)

	choice = input()
	if choice == '1':
		from kaytlyn1 import *
		questionone()
	elif choice == '3':
		from code import *
		q3()
	elif choice == '8':
		break 
	elif choice == '4':
		from code import *
		q4()
	elif choice == '2':
		from kaytlyn2 import *
		numbertwo()
	elif choice == '6':
		from kaytlyn3 import *
		numbersix()
