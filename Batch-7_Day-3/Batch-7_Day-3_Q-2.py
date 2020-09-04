for x in range(1,201):
	c=0
	for i in range(1,x+1):
		if x%i==0:
			c+=1
		if c>2:
			break
	if c==2:
		print(x)

