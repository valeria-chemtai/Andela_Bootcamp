def min_max(n):
    result=[]
    smallest=None
    largest=None
    firstrun=True

    for i in n:
        if firstrun or i<smallest:
            smallest=i
            firstrun=False

        elif largest==None or i>largest:
            largest=i

    if smallest==largest:
        result.append(smallest)
    else:
        result.append(smallest)
        result.append(largest)

    return result
