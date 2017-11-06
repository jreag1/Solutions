#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def answerfour():
	ans = 10201 #smallest eligible palindrome
	for a in range(999, 100, -1):
		for b in range(a, 100, -1):
			x = a * b
			if x > ans and str(x) == str(x)[::-1]:
					ans = x
	return ans
	
if __name__ == "__main__":
	print(answerfour())
	
#Returns 906609