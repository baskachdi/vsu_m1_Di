class Fract:
    def __init__(self, num = 1, denom = 1):
        self.num = num
        self.denom = denom
    def printfract (self):
           print(self.num,"/",self.denom)
    def inputfract (self):
        self.num = int(input("Введите числитель: "))
        self.denom = int(input("Введите знаменатель: "))
        while (self.denom == 0):
            if (self.denom == 0):
               print("знаменатель равный нулю недопустим.")
fract = Fract()
fract.printfract()
fract.inputfract()
fract.printfract()