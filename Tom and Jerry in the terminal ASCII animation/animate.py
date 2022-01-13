import pickle,time,os

with open('data.pickle','rb') as fp:
	frames=pickle.load(fp)

for frame in frames:
	print(''.join(frame))
	time.sleep(.040)
	os.system("clear")
