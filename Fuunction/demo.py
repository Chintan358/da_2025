
def msg():
    print("Hello world")

def square(a):
    print(a*a)

def add(a,b):
    return (a+b)
# k = add(10,20)

def person(name, email="test@gmail.com",phone="98898989"):
    print(name,email,phone)
           

def sum(*a):
    add  =0
    for i in a:
        add+=i
    print(add)

def subjects(**a):
    print(type(a))
    print(a)

# k = lambda a : a+a

# print(k(10))
# subjects(python="10",java="20")     
# sum(10,20,30,40,50,60)
# sum(10,20)
# msg()
# square(15)
# k = add(10,20)
# square(k)

# person("Sagar",phone="898989898")



