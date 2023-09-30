#!/usr/bin/python3
n = int(input("enter the row number:"))
list1 =[}
for i in range(n):
    temp_list=[]
    for j in range (i+1):
        if j==0 or j==i:
            tem_list.append(1)
        else:
            tem_list.append(list1[i-1][j-1] + list[i-1][j])
    list1.append(temp_list)
print(list1)

for i in range(n):
    for j in range(n-i-1):
        print(format" "<2"),end="")
    for j in range(i+1):
        print(format(list1[i][j],"<3"),end=" ")
    print()
