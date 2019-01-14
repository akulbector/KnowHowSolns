grades1 = [95,43,57,82,97,74,51,13,56,50,90]
grades2 = []
grades3 = []
grades4 = []


def avgPassingGrades(inputList):
    sublist = []
    count = 0
    sum = 0
    
    
    #for element in inputList
    for i in range(0, len(inputList)):
        #if(element>49):
        if(inputList[i]>49):
            #sum += element
            sum += inputList[i]
            count +=1
            
    return sum/count


def lowest(list):
    isThereALowest = False
    lowest=False
    
    for element in list:
        if(element>49):
            if (lowest==False):
                lowest=element
            elif (lowest>element):
                lowest=element
                
                
    return lowest
            
            
def sorting(list):
    sortedList = []
    copy = list.copy()
    
    #for element in copy:
     #   if (element<49):
      #      copy.remove(element)
    
    
    while (len(copy)>0):
        minVal = lowest(copy)
        copy.remove(minVal)
        sortedList.append(minVal)
        
    return sortedList
            
            

print(avgPassingGrades(grades1))
print(lowest(grades1))
print(sorting(grades1))