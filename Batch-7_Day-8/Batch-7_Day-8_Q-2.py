fileHandle=open("Example.txt","r")
print("Reading contents of the file....\n",fileHandle.read())
try:
	fileHandle.write("I want to add this text in the file")
except:
	print("File can not be written in, it is open with read only.")

#Output:
# Reading contents of the file....
#  HEEEEY!
# File can not be written in, it is open with read only.
