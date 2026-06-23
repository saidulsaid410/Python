n=int(input("Enter the number: "))
if n<=1:
    print(f'{n} is not prime number')
else:
    for i in range(2,n):
        if(n%i==0):
            print(f'{n} is not prime number')
            print(f'{i} is the factor of {n}')
            break
    else:
      print(f'{n} is prime number')