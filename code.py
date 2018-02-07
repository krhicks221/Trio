def q3():
	lst = []
	val = int(input('Enter your numbers:'))
	print(val)
	for i in range(val):
		vals = int(input('Enter preferred number:'))
		print(vals)
		lst.append(vals)
	print('Your value is:', min(lst))



