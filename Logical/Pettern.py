# *****
# *****
# *****
# *****
# *****

# lines = 5
# for j in range(lines):
#     for i in range(lines):
#         print("*",end="")   
#     print()

# *
# **
# ***
# ****
# *****


# lines = 10
# starts = 1
# for i in range(lines):
#     for j in range(starts):
#         print("*",end="")
#     print()
#     starts+=1

# *****
# ****
# ***
# **
# *


# lines = 5
# starts = lines
# for i in range(lines):
#     for j in range(starts):
#         print("*",end="")
#     print()
#     starts-=1

#     *
#    **
#   ***
#  ****
# *****


# lines = 10
# starts = 1
# spaces =lines-1
# for i in range(lines):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(starts):
#         print("*",end="")
#     print()
#     starts+=1
#     spaces-=1

# *****
#  ****
#   ***
#    **
#     *


# lines = 10
# starts = lines
# spaces = 0
# for i in range(lines):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(starts):
#         print("*",end="")
#     print()
#     starts-=1
#     spaces+=1

#     *
#    * *
#   * * *
#  * * * *
# * * * * * 


# lines = 10
# starts = 1
# spaces =lines-1
# for i in range(lines):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(starts):
#         print("*",end=" ")
#     print()
#     starts+=1
#     spaces-=1

#        *
#       ***
#      *****
#     *******
#    *********


# lines = 10
# starts = 1
# spaces =lines-1
# for i in range(lines):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(starts):
#         print("*",end="")
#     print()
#     starts+=2
#     spaces-=1


#        *
#       ***
#      *****
#     *******
#    *********
#    *********
#    *********
#    *********
#    *********

# lines = 21
# starts = 1
# spaces =lines-1
# mid = (lines//2)+1
# for i in range(1,lines+1):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(starts):
#         print("*",end="")
#     print()
#     if i<mid :
#         starts+=2
#         spaces-=1


#        *
#       ***
#      *****
#     *******
#    *********
#     *******
#      *****
#       ***
#        *

# lines = 5
# starts = 1
# spaces =lines-1
# mid = (lines//2)+1
# for i in range(1,lines+1):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(starts):
#         print("*",end="")
#     print()
#     if i<mid :
#         starts+=2
#         spaces-=1
#     else : 
#         starts-=2
#         spaces+=1
     
     

#        *
#       * *
#      *   *
#     *     *
#    *       *
#     *     *
#      *   *
#       * *
#        *
     

# lines = 11
# starts = 1
# spaces =lines-1
# mid = (lines//2)+1
# for i in range(1,lines+1):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(starts):
#         if j==0 or j==starts-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     if i<mid :
#         starts+=2
#         spaces-=1
#     else : 
#         starts-=2
#         spaces+=1


# *     *
# * * * *
# *  *  *
# * * * *
# *     *
