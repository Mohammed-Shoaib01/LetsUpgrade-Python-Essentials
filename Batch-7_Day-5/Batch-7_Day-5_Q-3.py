# using .capatilize() method on each word in a list of words with lambda function
capitalizeEveryWord=lambda listOfWords : map(lambda eachWord: eachWord.capitalize(), listOfWords)
#Using .split() method on each strings to get every word
listOfWords=lambda everyWord:everyWord.split()
#Using .join() method to join list of strings
joiningListOfSmallStrings=lambda capitalWords:' '.join(capitalWords)

listOfStrings=["hey this is shoaib","i am from hyderabad","this program is a little complex"]

#using map on y to map to listOfString and then mapping it to capitalizeEveryWord to capitalize every word, we then map this list of lists of strings to d rebuild the list
c=list(map(joiningListOfSmallStrings,(map(capitalizeEveryWord,list(map(listOfWords,listOfStrings))))))

print(c)

'''
Output:

['Hey This Is Shoaib', 'I Am From Hyderabad', 'This Program Is A Little Complex']

'''

