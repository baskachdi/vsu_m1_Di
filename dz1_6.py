def number(i):
    if i > 1:
        if i == 2 or i == 3:
            return True
        elif i % 2 == 0:
            return False
        for j in range(3, i+1):
            if i % j == 0 and i != j:
                return False
            elif i == j:
                return True 
    return False
#print(number(int(input('Введите пожалуйста если не сложно конечно: '))))
#print("Спасибо пожалуйста")