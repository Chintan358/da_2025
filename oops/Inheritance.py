
class A:

    a = 20
    def show(self):
        print("show",self.a)

class B(A) :
    def run(self):
        print("run",self.a)


# a = A()
# a.show()

b =B()
b.run()
b.show()