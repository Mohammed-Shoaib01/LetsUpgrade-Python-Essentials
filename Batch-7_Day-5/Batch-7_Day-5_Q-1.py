def num(LongList,subList):
	i=0
	for Elements in LongList:
		if LongList[i:i+len(subList)]==subList:
			print("It's a Match")
			return 		
		i=i+1
	print("It's Gone")
mainList=input("Please Enter a list of numbers with spaces in between each element :)")
mainList=[int(j) for j in mainList.split()]
subListToFind=[1,1,5]
num(mainList,subListToFind)



'''Output:

Please Enter a list of numbers with spaces in between each element :)5 6 5 4 5 6 5 4 5 6 6 5 1 1 5

It's a Match
'''