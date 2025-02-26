
number = 50

sum = 0
f=1
while number !=0:
    rem = number%2  #1
    sum +=rem*f #10011
    number = number//2 #3
    f*=10
  
print(sum)


