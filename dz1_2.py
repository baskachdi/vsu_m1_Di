def mounth(n: int):
    if int(n) < 13 and n==int(n) and int(n) > 0 : 
        k = {"Winter": [12, 1, 2], "Spring": [3, 4, 5],"Summer": [6, 7, 8],"Autumn": [9, 10, 11]}
        for i in k:
            if n in k[i]:
                return i
    else:
        return("Нет такого месяца")

#n = ""
#print(mounth(n))