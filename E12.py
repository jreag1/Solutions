#What is the value of the first triangle number to have over five hundred divisors?

def divisors_list(x):
	div = []
	for i in xrange(1, int(x**0.5)+1):
		if x%i == 0:
			div.append(i)
			div.append(x//i)
	return set(div)

def answertwelve():
	a = 1
	b = 1
	while len(divisors_list(a)) < 501:
		b = b+1
		a = a+b
	return a
	
if __name__ == "__main__":
	print(answertwelve())
	
#Returns 76576500.