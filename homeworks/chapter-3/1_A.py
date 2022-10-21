class Binary:
    def __init__(self, num,other):
        self.num=int(str(num),2)
        self.other=int(str(other),2)




    def add(self):
        a=self.num+self.other
        return bin(a)[2::]



    def sub(self):
        b=self.num - self.other
        return bin(b)[2::]

    def mul(self):
        m=self.num * self.other
        return bin(m)[2::]

    def floordiv(self):
        f=self.num//self.other
        return bin(f)[2::]

    def __str__(self):
        print(Binary.add(self), Binary.sub(self), Binary.mul(self), Binary.floordiv(self))
a=Binary(101,10)
str(a)


