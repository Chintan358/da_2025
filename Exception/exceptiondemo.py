# print("Program starting...")

# try:
#     a = 10
#     b = a/0
#     print(b)

#     # l = [10,20,30]
#     # print(l[6])
# except Exception as e:
#     print(e)
# # except ZeroDivisionError as z:
# #     print(z)
# # except IndexError as i:
# #     print(i)
# else:
#     print("else calling")
# finally:
#     print("always executable....")

# print("program ended")


# try : 
#     a = int(input("enter number : "))
#     print(a)
# except Exception as e:
#     print(e)

# d = {"python":"10","java":"102"}
# print(d['pythondff'])

# open("demp.txt",'r')


def test():
    try : 
        a = int(input("enter number : "))
        return 1
    except Exception as e:
        return 0
    finally:
        print("always executable...")


        
k = test()
print(k)