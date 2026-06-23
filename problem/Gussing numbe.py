import random
num=random.randint(1,10)
guss=int (input("Guess a number 1 to 10: "))
while guss!=num:
    if guss<num:
        print("Your guess is too low ")
    elif guss>num:
        print("Your guess is too high")
    guss =int(input("Guess again: "))
print("You gessed it right")