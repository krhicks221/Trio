menu = """

1. Reverse a string
2. Reverse a sentence
3. Find the minimum value in a list
4. Find the maximum value in a list
5. Calculate the remainder of a given numerator and denominator
6. Return distinct values from a list including duplicates 
7. Return distinct values and their counts
8. Given a string of expressions and a set of variable/value pairs, return the result of the expression
9. Exit menu
""" 

while(True):
	print(menu)

	choice = input()

	if choice == '3':
		from code import *
		q3()
	elif choice == '9':
		break 

