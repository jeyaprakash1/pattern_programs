# - - - - - 1
# - - - - 1
# - - - 1
# - - 1
# - 1
i=1
for row in range(5,0,-1):
    for col in range(1,row+1):
        print('-',end="")
    print(i,end="")
    i+=1
    print()
   
