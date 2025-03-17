
class Pen:
   
    a = 10
    def __init__(self,id,name):
        self.id  =id
        self.name = name

    def test(self):
        print(self.id, self.name)

    @staticmethod
    def disp():
        print("display calaling",a)
    
    @classmethod
    def demo(self):
        print("Running demo",self.a)

p = Pen(10,"Sagar")
p.test()

p1 = Pen(20,"Swapnil")
p1.test()

p2 = Pen(30,"Meet")
p2.test()

Pen.disp()
Pen.demo()

