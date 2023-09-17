from art import logo, vs
from game_data import data
import random, os

print(logo)

person1 = random.choice(data)
person2 = random.choice(data)
if person1 == person2:
    person2 = random.choice(data)
print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
print(vs)
print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")

user_score = 0
while True:
    user_choice = input("Who has more followers? 'A' or 'B': ").lower()

    if person1['follower_count'] > person2['follower_count']:
        correct_answer = person1
        wrong_answer = person2
    else:
        correct_answer = person2
        wrong_answer = person1

    if user_choice == 'a':
        user_answer = person1
    else:
        user_answer = person2

    if user_answer == correct_answer:
        person1 = wrong_answer
        user_score += 1
    else:
        print(f"Sorry, that's wrong. Final score: {user_score}")
        exit()

    os.system('clear')

    print(logo)
    print("You are right. Current Score: {}".format(user_score))
    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
    print(vs)
    person2 = random.choice(data)
    print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")

    
