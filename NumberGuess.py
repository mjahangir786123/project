import random


number = input("Type a number: ")

if number.isdigit():
    number = int(number)

    if number <= 0:
        print("Type a number larger then 0")
        quit()
else:
        print("Type a number only")
        quit


random_number =  random.randint(0, 11)
guess= 0
while True:
        guess += 1
        user_guess= input("Make a guess? ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a number next time ")

        if user_guess == random_number:
            print("Awesome!! You guess in ",  guess, "guesses ")
            quit()
        elif user_guess > random_number:
            print("Type a number less then your guess")
        else: 
            user_guess < random_number
            print("Type a number higher then guess")



  