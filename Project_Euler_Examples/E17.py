'''If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.'''

def answerseventeen():
	a = (len('thousand') + 900*len('hundred') + 9*99*len('and') + 100*len('ninety')
	+ 100*len('eighty') + 100*len('seventy') + 100*len('sixty') + 100*len('fifty')
	+ 100*len('forty') + 100*len('thirty') + 100*len('twenty') + 10*len('nineteen')
	+ 10*len('eighteen') + 10*len('seventeen') + 10*len('sixteen') + 10*len('fifteen')
	+ 10*len('fourteen') + 10*len('thirteen') + 10*len('twelve') + 10*len('eleven') + 10*len('ten')
	+ 191*len('one') + 190*len('two') + 190*len('three') + 190*len('four') + 190*len('five')
	+ 190*len('six') + 190*len('seven') + 190*len('eight') + 190*len('nine'))
	return a
			
if __name__ == "__main__":
	print(answerseventeen())
	
#Returns 21124.