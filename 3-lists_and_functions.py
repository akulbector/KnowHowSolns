grades1 = [95,43,57,82,97,74,51,13,56,50,90]
grades2 = []
grades3 = []
grades4 = []

#Averages all grades above 49
def avgPassingGrades(inputList):
    #Creates a sum and count variable since sum/count = average
    count = 0
    sum = 0
    
    
    #for element in inputList
    for i in range(0, len(inputList)):
        #If the element is passing grade
        #if(element>49):
        if(inputList[i]>49):
            #Then include it in the average calculation
            #sum += element
            sum += inputList[i]
            count +=1
            
    return sum/count

#Returns the lowest grade above 49
#If there is no grade above 49, function returns false
def lowest(list):
    #Sets lowest=False initially, since if there is no grade above 49, the function will return false
    lowest=False
    
    for element in list:
        if(element>49):
            if (lowest==False or lowest>element):
                lowest=element
                
                
    return lowest
            
#Sorts all passing grades            
def sorting(list):
    #List to output
    sortedList = []
    #Creates a copy to keep the original list untouched
    copy = list.copy()
    
   
    #Repeatedly finds the lowest passing grade, removes it from copy of the input list, and appends it into the output list
    while (len(copy)>0):
        minVal = lowest(copy)
        copy.remove(minVal)
        sortedList.append(minVal)
        
    return sortedList
            
            

print(avgPassingGrades(grades1))
print(lowest(grades1))
print(sorting(grades1))
