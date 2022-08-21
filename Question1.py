class Power:
    def __init__(self, x, y):#x = base and y = exponent
        self.x = x
        self.y = y
    def Power_value(self):
        return self.x**self.y
a = Power(10,2)
print(a.Power_value())