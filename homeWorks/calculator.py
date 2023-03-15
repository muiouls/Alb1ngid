class Calk:
    def __init__(self,numberone ,numbertwo):
        self.numberone = numberone
        self.numbertwo = numbertwo

    def __add__(self):
        return self.numberone + self.numbertwo

    def __sub__(self):
        return self.numberone - self.numbertwo

    def __mull__(self):
        return self.numberone * self.numbertwo

    def __truediv__(self):
        return self.numberone / self.numbertwo


on =Calk(15 ,45)
print(on.__add__())
print(on.__sub__())
print(on.__mull__())
print(on.__truediv__())