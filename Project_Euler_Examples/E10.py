#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import math
def is_prime(number):
	n = int(math.sqrt(number))
	if number%2 == 0:
		return False
	else:
		for y in range(3,n+1,2):
			if number%y == 0:
				return False
				break
	return True

def answerten():
	answer=2
	for i in xrange(3,2000000, 2):
		if is_prime(i):
			answer += i
	return answer
	
if __name__ == "__main__":
	print(answerten())
	
#Returns 142913828922.