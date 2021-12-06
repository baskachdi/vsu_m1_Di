import dz1_1
def copy_():
    k = dz1_1.list_()
    k.sort()
    while k != []:
        print(k[0], "встречается", k.count(k[0]), "раза")
        for i in range(k.count(k[0])):
            k.remove(k[0])
#print(k)

copy_()