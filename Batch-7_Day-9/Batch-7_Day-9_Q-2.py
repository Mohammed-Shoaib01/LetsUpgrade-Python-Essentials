 
def armStrongNumber(l):
	for n in l:
		temp=n
		s=0
		while temp>0:
			r=int(temp%10)
			s+=int(r*r*r)
			temp=int(temp)/10
		if n==s:
			yield n
print("This is a list of Armstrong Numbers between 1 to 1000: ",list(armStrongNumber(list(range(1,1000)))))

#Output:
#This is a list of Armstrong Numbers between 1 to 1000:  [1, 153, 370, 371, 407]

