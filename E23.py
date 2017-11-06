#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def divisors_list_sum(x):
	div = [1]
	for i in xrange(2, int(x**0.5)+1):
		if x%i == 0:
			div.append(i)
			div.append(x//i)
	return sum(set(div))

def abundant_list(y):
	return divisors_list_sum(y) > y
	
def answertwentythree():
	ans = 0
	abundant = set()
	for j in xrange(1,28123):
		if abundant_list(j):
			abundant.add(j)
		if not any((j - item in abundant) for item in abundant):
				ans += j
	return ans
				
if __name__ == "__main__":
	print(answertwentythree())

#Returns 871198282.