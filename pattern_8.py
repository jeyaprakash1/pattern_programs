# 5 5 5 5 5
#   4 4 4 4
#     3 3 3
#       2 2
#         1

for row in range(5,-1,-1):
    for col in range(5,row,-1):
        print(' ',end=" ")
    for col2 in range(1,row+1):
        print(row,end=" ")
    print()
