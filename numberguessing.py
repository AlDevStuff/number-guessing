import random

num = random.randint(0, 20)
m = ""

while m != num: 
        m = int(input("Guess the number: "))

        if m == num: 
            print("You have guessed it correctly!")
            break
        if m < num: 
            print("Too small.")
        if m > num: 
            print("Too big.")