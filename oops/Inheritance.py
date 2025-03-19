
class A:

    a = 20
    def show(self):
        print("show",self.a)

class B() :
    def run(self):
        print("run",self.a)

class C(A,B):
    def disp(self):
        print("disp calling",self.a)

class D(C):
    pass

# a = A()
# a.show()

# b =B()
# b.run()
# b.show()