from math import sqrt
c=299792458 #speed of light in m/s

t=eval(input("Enter the time passed on earth in year: "))
v=c
while not v<c:
	v=eval(input("Enter the speed of the object in m/s: "))
	if v>c:
		print("Speed of the object must be less than the speed of light:",c)
def time_dialation(c,v,t):
	t_0=t*sqrt(1-(v**2/c**2))
	return t_0
print("time passed to the object",time_dialation(c,v,t)," year")
		
