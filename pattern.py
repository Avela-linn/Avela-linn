#Use loop function to create pattern
# i is for column anf j is for row
# do reverse to create the pattern

print("*")
for i in range(5):
    for j in range(i+1):
        print("*",end="")
        print()


for i in range(5):
    for j in range(i,5):
        print("*",end=" ")
        print()

