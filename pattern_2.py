# 5
# 5 4
# 5 4 3 
# 5 4 3 2
# 5 4 3 2 1

for row in range(5,-1,-1):
    for col in range(5,row,-1):
        print(col,end="")
    print()
