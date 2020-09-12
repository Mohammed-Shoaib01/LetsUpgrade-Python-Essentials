#Print all prime numbers between two given numbers using decorators

def getStartAndEndPointForList(anyFunc):
	def WrapFunc():
		startPoint=int(input("Enter starting point for list"))
		endPoint=int(input("Enter end point for list"))
		for r in range(startPoint,endPoint+1):
			anyFunc(r)
	return WrapFunc
@getStartAndEndPointForList
def Prime(checkNumber):
	FactorsCount=0
	for n in range(1,checkNumber+1):
		if checkNumber%n==0:
			FactorsCount=FactorsCount+1
	if FactorsCount==2:
		print(checkNumber,"is a prime number")
Prime()


#Output:
# Enter starting point for list1
# Enter end point for list50
# 2 is a prime number
# 3 is a prime number
# 5 is a prime number
# 7 is a prime number
# 11 is a prime number
# 13 is a prime number
# 17 is a prime number
# 19 is a prime number
# 23 is a prime number
# 29 is a prime number
# 31 is a prime number
# 37 is a prime number
# 41 is a prime number
# 43 is a prime number
# 47 is a prime number
