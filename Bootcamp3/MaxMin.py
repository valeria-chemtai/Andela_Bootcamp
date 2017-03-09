def find_max_min(n):
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
        a=[smallest]

    else:
        a=[smallest,largest]

    return a