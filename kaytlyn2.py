#Sentence Reversal
def numbertwo():
	sentence = input("Give us a sentence, please! ") #Defines the sentence variable as the input of the user after being asked to input a sentence
	new = sentence.split() #splits the inputted sentence into seperate strings ("Hello", "cruel", "world")

	result = [] #The brackets turn the result variable into a list
	x = len(new) - 1 #determines the length of the new variable and removes the last word
	while x >= 0:
		result.append(new[x]) #moves the word at the end of the list/sentence to the front of the list/sentence
		x = x - 1 #moves around the words in the list/sentence

	result = " ".join(result) #joins together the previously split string in reverse
	print(result) #prints the newly reversed sentence
