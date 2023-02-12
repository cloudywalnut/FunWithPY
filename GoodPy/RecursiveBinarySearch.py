MyData = [9,15,25,32,48,55,63,67,72,80]

def BinarySearch(SearchValue,Top,Bottom):

    Middle = int((Top+Bottom)/2)

    if Top > Bottom:
        print ("Data not found") #Base Case
    elif SearchValue == MyData[Middle]:
        print (Middle) #Base case
    elif SearchValue > MyData[Middle]:
        BinarySearch(SearchValue, (Middle + 1), Bottom) #General Case
    elif SearchValue < MyData[Middle]:
        BinarySearch(SearchValue, Top, (Middle-1) ) #General Case
    
print (BinarySearch(90, 0, 9))