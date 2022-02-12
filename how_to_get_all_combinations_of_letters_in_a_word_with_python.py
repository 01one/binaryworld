from itertools import permutations
word=str(input("Enter your word: "))
l=len(word)+1
combinations=[]
for i in range(1,l):
	a=list(permutations(word,i))
	for element in a:
		x=(''.join(element))
		combinations.append(x)
print(combinations)
