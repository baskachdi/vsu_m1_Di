class Fract:
    def __init__ (self, num = 0, denom = 0):
        self.num = num
        self.denom = denom
    def inputfract (self):
        self.num = int(input("Введите числитель: "))
        self.denom = int(input("Введите знаменатель: "))
    def printfract (self):
        print(self.num,"/",self.denom)
        
fract = Fract()
fract.inputfract()
fract.printfract()
