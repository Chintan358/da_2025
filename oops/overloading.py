from multipledispatch import dispatch

class Calc:

    @dispatch(int ,int)
    def add(self,a,b):
        print("result is 1:",a+b)
    
    @dispatch(int,int,int)
    def add(self,a,b,c):
        print("result is 2:",a+b+c)

    @dispatch(int,float)
    def add(self,a,b):
        print("result 3 : ",a+b)


c = Calc()
c.add(10,20)
c.add(10,20,30) 
c.add(20,30)