#Reverse a single word string

def questionone():
	def reverse(ouch): #defines the reversal function
		str = " " #whatever is put in is a string
		for i in ouch:
			str = i + str #the reversal
		return str #returns the string reversed

	ouch = input("Enter a word, please! ") #tells you what to do and allows you to input your word, also defining the ouch variable
	print(" ", ouch) #prints your inputted string from the ouch variable input
	print("Reverse, reverse! ", reverse(ouch)) #prints the reversed version of your inputted string from the ouch variable input
