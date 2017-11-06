#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def answersix():
	a = sum(x for x in range(1,101))**2
	b = sum(x**2 for x in range(1,101))
	return a-b
	
if __name__ == "__main__":
	print(answersix())
	
#Returns 25164150