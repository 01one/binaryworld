x=int(input("How many fibonacci numbers do you want:"))
number1=0
number2=1
for i in range(x):
	print(number1)
	number=number1+number2
	number1=number2
	number2=number
