class Fract:
    def __init__(self, num = 0, denom = 0):
        self.num = num
        self.denom = denom
    def inputfract (self):
        self.num = int(input("Введите числитель: "))
        while (self.denom == 0):
            self.denom = int(input("Введите знаменатель: "))
            if (self.denom == 0):
               print("знаменатель равный нулю недопустим.")
fract = Fract()
fract.inputfract()
fract.printfract()