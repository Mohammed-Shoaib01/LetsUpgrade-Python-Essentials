#List and its default funtions.

juicemix=["apple","mango","banana","grapes","oranges"]
#print total list
print(juicemix)
#print 2nd element of list
print(juicemix[1])
#print last element of list
print(juicemix[-1])
#print reverse of a list
print(juicemix[::-1])
#print sublist
print(juicemix[1:3])
#FUNCTIONS OF LIST

print(juicemix)

#append() method
juicemix.append("melon")
print(juicemix)

#insert() method
juicemix.insert(4,"cherry")
print(juicemix)


#remove() method
juicemix.remove("apple")
print(juicemix)


#pop() method
juicemix.pop()
print(juicemix)

#copy() method
mixer=juicemix.copy()
print(juicemix)

#sort() method
juicemix.sort()
print(juicemix)

#clear() method
juicemix.clear()
print(juicemix,"\n\n\n")




#Dictionaries and its default funtions.

marks={"Maths":"75","English":"63","Science":"80","Physics":"50"}

#FUNCTIONS OF Dict

print(marks)

#get() method
print(marks.get("Maths"))

#update() method
marks.update({"Chemistry":"80"})
print(marks)


#pop() method
marks.pop("Science")
print(marks)


#popitem() method
marks.popitem()
print(marks)

#copy() method
Report=marks.copy()
print(Report)

#values() method
print(marks.values())

#clear() method
marks.clear()
print(marks,"\n\n\n")



#Sets and its default funtions.


AdminNo={171,173,175,177,179}

print(AdminNo)

AdminNo.add(181)

print(AdminNo)

AdminNo.copy

print(AdminNo)

AdminNo.discard(179)

print(AdminNo)

AdminNo.pop()

print(AdminNo)

AdminNo.clear()

print(AdminNo,"\n\n\n")


T=(23,18,19,23,19,22)
print(T)
print(T.count(19))
print(T.index(22))
print(T[-1])
print(T[0],"\n\n\n")
X=T+T
#Delete tuple
del T


#Strings and its default funtions.
x="Hey! I am a string"
print(x.upper())
print(x.lower())
print(x.count(" "))
print(x.capitalize())
print(x.find("I"))


