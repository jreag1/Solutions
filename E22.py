'''Using names.txt, (work) out the alphabetical value for each name,
 multiply this value by its alphabetical position in the list to obtain a name score.
What is the total of all the name scores in the file?'''

def answertwentytwo():
	f = open("p022_names.txt","r")
	namelist = []
	namelist = f.readline().replace('\"','').split(',')
	namelist.sort()
	namelist_fin = enumerate(namelist)
	alpha_value = {"A": 1,"B": 2,"C": 3,"D": 4,"E": 5,"F": 6,"G": 7,"H": 8,"I": 9,"J": 10,"K": 11,"L": 12,
	"M": 13,"N": 14,"O": 15,"P": 16,"Q": 17,"R": 18,"S": 19,"T": 20,"U": 21,"V": 22,"W": 23,"X": 24,"Y": 25,"Z": 26}
	ans=0
	for num,name in namelist_fin:
		n = 0
		for x in name:
			n += alpha_value[x]
		ans += n*(num + 1)
	return ans
				
if __name__ == "__main__":
	print(answertwentytwo())

#Returns 871198282.