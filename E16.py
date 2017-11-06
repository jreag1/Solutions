#What is the sum of the digits of the number 2^1000?

def answersixteen():
	num = str(2**1000)
	ans = 0
	for x in xrange(0, len(num)):
		ans += int(num[x])
	return ans
			
if __name__ == "__main__":
	print(answersixteen())
	
#Returns 1366.