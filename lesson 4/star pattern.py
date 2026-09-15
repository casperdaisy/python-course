#python program to print the star pattern based on the number of rows specified by the user
#get the number of rows from user
n = int(input("enter the number of rows:"))
#outer loop for each row
for i in range (1,n+1):
    #inner loop for each column in the row
    for j in range(i):
        #print star,end with space instead of new line
        print('*',end=' ')
        #After each row print a new line
    print()