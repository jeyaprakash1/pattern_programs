# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 1112131415

i=1
for row in range(1,6):
    for col in range(row):
        print(i,end="")
        i=i+1
    print()
