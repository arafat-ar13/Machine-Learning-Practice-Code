from random import randint
from time import sleep

print("Welcome! Please enter a number between 2 and 10")

sleep(1)
user_guess = int(input("Please enter your guess: "))
real_number = randint(2,10)
user_attempts = 5

while user_guess != real_number:
    if user_attempts == 1:
        sleep(0.23)
        print(f"You used all your attempts. {user_attempts} is what's left. You are a loser.")
        break 
    if user_guess > real_number:
        user_attempts -= 1
        sleep(1)
        print(f"You have {user_attempts} attempts left")
        sleep(1)
        user_guess = int(input("Your guess was too high. Please try a lower number: "))
    elif user_guess < real_number:
        user_attempts -= 1
        sleep(1)
        print(f"You have {user_attempts} attempts left")
        sleep(1)
        user_guess = int(input("Your guessed too low. Try upping it a bit: "))
if user_guess == real_number:
    sleep(1)
    print("You won!")
      
