'''
Sept 29, 2019
CSC246, Programming Languages
Dr. Kendall-Morwick
Jonathan Webber

        Functional Programming
'''

def allsubsets(newSet):

    #convert the input set into a list
    tempList = list(newSet)

    #create a newList to return
    newList = []

    #get the length of the input set/list and determine the number of iterations to do
    length = len(tempList)
    iterations = 2**length
    
    #get the length of the largest binary number from the iterations
    sizeBinString = len(bin(iterations-1).replace('0b',''))

    #if the user inputs the emptyset
    if length == 0:

        yield frozenset({})

    else:

        #go from after the empty set through all iterations
        for x in range(1,iterations):

            #append to the newList the frozen subset
            yield subset(tempList,x,sizeBinString)
    

#function to create a frozenset for a subset
def subset(tempList,count,sizeBinString):

    #create a binary string by putting zeroes in front if need be
    binString = putzeroes((bin(count).replace('0b','')),sizeBinString)

    #create the empty list to return
    returnList = []

    #go through all indexes in the tempList
    for i in range(0,sizeBinString):

        #if there is a 1 in the binary string, put that number in the list to return
        if binString[i] == '1':
            returnList.append(tempList[i])

    return frozenset(returnList)

#function to put the correct amount of zeroes on a binary string to make it work with the above function
def putzeroes(binstring,length):
        return ('0'*(length - len(binstring)) + binstring) if len(binstring) < length else binstring
