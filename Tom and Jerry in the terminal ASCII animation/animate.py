import pickle,time,os

with open('data.pickle','rb') as fp:
	frames=pickle.load(fp)

for i in range(1):
	for frame in frames:
		print(''.join(frame))
		time.sleep(.040)
		os.system("clear")
		#os.system("cls") #if you are in windows(command prompt)
