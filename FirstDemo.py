class Calculator:
    num = 100

    def __init__(self,a,b):
        self.a = a
        self.b = b
    def getData(self):
        print("Hello world how are you!")

    def sum(self):
        return self.a+self.b

obj = Calculator(2,3)
obj.getData()
print(obj.num)
print(obj.sum())
