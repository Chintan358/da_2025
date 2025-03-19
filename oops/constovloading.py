

class Demo:

    def __init__(self,*a):
        print(a)
    
    def add(self,*a):
        sum = 0
        for i in a:
            sum+=i
        print(sum)

d = Demo(10)
d1 = Demo(10,20)

d.add(10,20)
d.add(10,20,30)