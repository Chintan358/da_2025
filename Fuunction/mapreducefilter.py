l = [10,20,30,40,50,60]
l1 = [1,2,3,4,5,6]

# for i in l:
#     l1.append(i*i)
# print(l1)


import math

# def square(a,b):
#     return math.pow(a,b)

# l1 = map(square,l,l1)
# print(list(l1))

k = map(math.pow,l,l1)
print(list(k))