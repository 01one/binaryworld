a=eval(input("Enter a number to see the squareroot:"))
b=0
x=(1+a/1)/2
while b!=10: #we 'll count 10 decimal places
	b+=1
	x=(x+a/x)/2
print(x)
