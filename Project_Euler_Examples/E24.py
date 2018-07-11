#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
	
import itertools	
	
def answertwentyfour():
	perm_list = list(itertools.permutations("0123456789"))
	ans = perm_list[999999]
	return ''.join(ans)
				
if __name__ == "__main__":
	print(answertwentyfour())

#Returns 2783915460.