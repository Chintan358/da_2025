# l = [10,20,30,40,50,60]
# l1 = [1,2,3,4,5,6]

# for i in l:
#     l1.append(i*i)
# print(l1)


# import math

# def square(a,b):
#     return math.pow(a,b)

# l1 = map(square,l,l1)
# print(list(l1))

# k = map(math.pow,l,l1)
# print(list(k))


# def add(a):
#     return a+2

# def mul(a):
#     return a*a

# def apply(func,a):
#     return func(a)


# k = apply(add,10)
# l = apply(mul,10)

# print(k)
# print(l)


# l = [10,20,30,40,50]

# def square(a):
#     return a*a

# # l1 = map(square,l)
# l1 = map(lambda x:x*x,l)
# print(list(l1))

# import math
# k = [4,9,16,25,36,49]

# k1 = map(lambda x:math.sqrt(x),k)
# print(list(k1))


# a = [10,20,30,40,50]
# b = [1,2,3,4,5,]

# l1 = map(lambda x,y:x**y,a,b)
# print(list(l1))


# a = [1,5,6,78,4,5,3,9]

# b = filter(lambda x: x%2!=0 ,a)
# print(list(b))

# data = [0, 1, 4, 6, 8, 9, 10, 12, 16, 81, 23, 36]  

# import math

# k = filter(lambda x :math.sqrt(x).is_integer(),data)
# print(list(k))

# names = ["Sagar","Swapnil","Hinali","Meet","Prem"]

# l = filter(lambda x: x.startswith('S'),names)
# print(list(l))

from functools import reduce  

l = [10,20,30,40,50]

def add(x,y):
    return x+y

k = reduce(add,l)
print(k)