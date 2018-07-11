#What is the 10 001st prime number?

import math
def is_prime(number):
	k = int(math.sqrt(number))
	if number%2 == 0:
		return False
	else:
		for y in range(3,k+1,2):
			if number%y == 0:
				return False
				break
	return True

def answerseven():
	primes = [2]
	n = primes[-1]
	while len(primes) < 10001:
		n = n+1
		if is_prime(n):
			primes.append(n)
	return primes[-1]
	
if __name__ == "__main__":
	print(answerseven())
	
#Returns 104743.