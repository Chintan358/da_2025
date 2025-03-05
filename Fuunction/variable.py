
a = 10

def test():
    global a
    a = 20
    print(a)


# print(a)  //10 10
# test()    //20 20
# print(a)  //10 20

