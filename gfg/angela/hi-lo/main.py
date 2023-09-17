import random

difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")

if difficulty == 'hard':
    number_of_attempts = 5
else:
    number_of_attempts = 10

print(f"You have {number_of_attempts} attempts remaining to guess the number.")

correct_number = random.randint(1, 100)

while True:
    player_guess = int(input("Make a guess: "))
    
    if player_guess == correct_number:
        print("Well done, you guessed it right!")
        break
    elif player_guess > correct_number:
        print("Guess Low")
    else:
        print("Guess High")

    number_of_attempts -= 1

    if number_of_attempts == 0:
        print("You have run out of attempts. Try again.")
        break