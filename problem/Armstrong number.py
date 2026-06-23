n=int(input("Enter the number: "))
sum=0
temp=n
while temp!=0:
    d=temp%10
    sum+=d**3
    temp//=10
if(n==sum):
    print(f"{n} Armstrong number")
else:
    print(f"{n} is nOt Armstrong number")
