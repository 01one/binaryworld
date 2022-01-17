from nltk import tokenize
s = open('data/Rationalization.txt').read()
x=tokenize.sent_tokenize(s)
for i in range(len(x)-1):
	print(x[i],'\n')
