#Number List Thing
def numbersix():
	result = set(input("Give a list of numbers, please! ")) #set the result variable as the input of the user and turns it into a set rather than a list

	for i in result:
		if i not in result:
			result.append()
#Takes out duplicates from the inputted list and adds everything into the set
	print(sorted(result)) #prints out the sorted set of inputted words and numbers without duplicates
