i=1042000
f=0
while i<702648265: 
	n=i
	temp=n
	s=0
	print(i," ",n)

	while temp>0:
		r=int(temp%10)
		s+=int(r*r*r)
		temp=int(temp)/10

	if n==s:
		print("\n",i,"is an Armstrong numbers")
		f=f+1
		break
	i+=1
if f==1:
	print("There are no armstrong numbers between 1042000 and 702648265")
#There are no Amrstrong numbers between 1042000 and 702648265