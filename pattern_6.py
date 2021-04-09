#         5     
#       4 4 
#     3 3 3
#   2 2 2 2
# 1 1 1 1 1

row=5
while row>=1:
    col=1
    while col<row:
        print(" ",end=" ")
        col+=1
    col2=5
    while col2>=row:
        print(row,end=" ")
        col2-=1
    print()
    row-=1
