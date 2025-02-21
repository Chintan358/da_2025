# 0 1 1 2 3 5 8 13 21 34 55 89 153 234 387


a = 0
b = 1
length = 18
print(a,b,end=" ")

# for i in range(length):
#     c  = a+b
#     print(c,end=" ")
#     a = b
#     b = c

while length!=0:
    c  = a+b
    print(c,end=" ")
    a = b
    b = c
    length-=1