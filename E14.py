#Which starting number, under one million, produces the longest (Collatz Sequence)?

def answerfourteen():
	m = 0
	n = 0
	for x in xrange(1,1000000):
		a = x
		b = 1
		while a > 1:
			if a%2 == 0:
				a = a/2
				b+=1
			else:
				a = 3*a+1
				b+=1
		if b > n:
			m = x
			n = b
	return m
			
			
	
if __name__ == "__main__":
	print(answerfourteen())
	
#Returns 837799.