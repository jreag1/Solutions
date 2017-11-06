#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import fractions

def lcm(a,b):
    return a*b//fractions.gcd(a,b)

def answerfive():
	return reduce(lcm, range(1,21))
	
if __name__ == "__main__":
	print(answerfive())
	
#Returns 232792560