#Find the sum of the digits in the number 100! (factorial). 

import math

def answertwenty():
	num = str(math.factorial(100))
	ans = 0
	for x in xrange(0, len(num)):
		ans += int(num[x])
	return ans
			
if __name__ == "__main__":
	print(answertwenty())
	
#Returns 648.