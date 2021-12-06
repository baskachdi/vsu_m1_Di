def list_ ():
    k = []
    s = input("Введите строку: ")
    while s.strip():
        k.append(s)
        s = input("Введите строку: ")
    return k

#print(list_())