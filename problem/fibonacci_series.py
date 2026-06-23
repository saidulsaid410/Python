item=int (input("Enter the number of fibonacci series: "))
n1,n2=0,1
for i in range(item):
    print(n1,end=' ')
    n=n1+n2
    n1=n2
    n2=n