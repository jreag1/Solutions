#Evaluate the sum of all the amicable numbers under 10000.

def divisors_sum(x):
	div = [1]
	for i in xrange(2, int(x**0.5)+1):
		if x%i == 0:
			div.append(i)
			div.append(x//i)
	return sum(set(div))

def answertwentyone():
	amicable = []
	for x in xrange(2,10000):
		for y in xrange(2,x):
			if divisors_sum(y) == x and divisors_sum(x) == y:
				amicable.append(x)
				amicable.append(y)
	return sum(set(amicable))
				
if __name__ == "__main__":
	print(answertwentyone())

#Returns 31626. This script would be quite slow for large numbers (to beginners: why?), but works well in this case. 