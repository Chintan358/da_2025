

# def decorator(func):
#     def wrap():
#         print("before...")
#         func()
#         print("after")
#     return wrap


def before(func):
    def wrap():
        print("print before something....")
        func()
    return wrap

def after(func):
    def wrap(*a):
        func(*a)
        print("print before something....")
    return wrap

def add(func):
    def sum(*a):
        func(*a)
        sum =0
        for i in a:
            sum+=i
        print("Sum is : ",sum)
    return sum

@before
def test():
    print("Testing something...")


@add
def home(a,b):
    print("welcome home")


# test()
home(10,30)