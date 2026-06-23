n=int (input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(1,n+1-i):
            print(end=' ')
    for s in range(1,1+i):
            print("*",end=' ')
    print(" ")

for k in range(1,n+1):
    for j in range(1,n-k+1):
       print(end=' ')
    for star in range(1,k+1):
        print("*",end=' ')
    print(' ')