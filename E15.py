'''Starting in the top left corner of a 2x2 grid, and only being able to move
 to the right and down, there are exactly 6 routes to the bottom right corner.
 How many such routes are there through a 20x20 grid?'''

import math
 
def answerfifteen():
	a = 20 #grid size
	b = 40 #total moves to reach corner
	return math.factorial(b)/(math.factorial(a)*math.factorial(b-a))
			
if __name__ == "__main__":
	print(answerfifteen())
	
#Returns 137846528820.