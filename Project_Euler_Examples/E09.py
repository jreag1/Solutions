#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def answernine():
	for x in range(1,1000):
		for y in range(x,1000-x):
			z = 1000 - x - y
			if x**2 + y**2 == z**2:
				return x*y*z
	
if __name__ == "__main__":
	print(answernine())
	
#Returns 31875000.