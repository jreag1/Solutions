#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math

def answerthree():
	a = 600851475143 
	b = int(math.floor(math.sqrt(a)))
	for x in range(2,b+1):
		while a % x == 0:
			a //= x
			if a == x or a == 1:
				return x
	
if __name__ == "__main__":
	print(answerthree())
	
#Returns 6857