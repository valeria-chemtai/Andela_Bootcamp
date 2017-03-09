def min_max(n):
    result = []
    smallest = None
    largest = None
    firstrun = True #Initializing a True condition to aid in looping

    for i in n:
        if(firstrun or i < smallest): #considering the first time of checking through the list
            smallest = i            #After moving through the list and finding a value that is smaller, set small to be that value
            firstrun = False     #our condition is set to false since a smaller value exists as compared to the first one

        elif largest == None or i > largest:
            largest = i

    if (smallest == largest):
        result.append(smallest)
    else:
        result.append(smallest)
        result.append(largest)

    return result
