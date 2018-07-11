#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
	
def answertwentyfive():
	a = 1 #First term
	b = 2 #Second term
	c = 1 #Term index
	while len(str(a)) < 1000:
		c +=1
		a, b = b, a+b
	return c+1
				
if __name__ == "__main__":
	print(answertwentyfive())

#Returns 4782.