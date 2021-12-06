def sred_ (k=[6, 6, 6 , 6, 6, 6]):
    s = 0
    for i in k:
        s = s + int(i)
    return s/len(k)

#print(sred_(k=[]))