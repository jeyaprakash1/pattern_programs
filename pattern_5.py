# 5
# 4 4 
# 3 3 3 
# 2 2 2 2
# 1 1 1 1 1 

val=5
for row in range(1,6):
    for col in range(1,row+1):
        print(val,end="")
    val-=1
    print()
