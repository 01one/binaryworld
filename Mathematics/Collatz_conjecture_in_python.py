#  Copyright 2022 Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY
def calculate(x):
	n=x
	conjecture=[]
	while n!=1:
		if n%2==0:
			n/=2
			conjecture.append(int(n))
		elif n>1 and n%2!=0:
			n=n*3+1
			conjecture.append(int(n))
		else:
			n=1
	return conjecture

for i in range(1,100001):
	print("Number= {}".format(i))
	c=(calculate(i))
	print(c)
	print("=============================================================")
