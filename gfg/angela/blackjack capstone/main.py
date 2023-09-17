import random

def deal_card(player_cards: list):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card  = random.choice(cards)
    if card == 11 and sum(player_cards) > 10:
        player_cards.append(1)
    else:
        player_cards.append(card)
    return
    

def play_game():
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if start_game == 'y':
        start_game = True
    else:
        start_game = False

    while start_game:
        playerCards = []
        computerCards = []

        deal_card(playerCards)
        deal_card(playerCards)
        deal_card(computerCards)
        deal_card(computerCards)

        playerScore = sum(playerCards)
        computerScore = sum(computerCards)

        if len(playerCards) == 2 and playerScore == 21:
            print(f"\tBlackJack! Your cards: {playerCards}, current score: {playerScore}")        
        else:
            print(f"\tYour cards: {playerCards}, current score: {playerScore}")
        
        print(f"\tComputer's first card: {computerCards[0]}")

        while True:
            another_card = input("Type 'y' to get another card, 'n' to pass: ")

            if another_card == 'y':
                deal_card(playerCards)
                playerScore = sum(playerCards)
                print(f"\tYour cards: {playerCards}, current score: {playerScore}")
                if playerScore > 21 and 11 in playerCards:
                    playerCards.remove(11)
                    playerCards.append(1)
                    playerScore = sum(playerCards)
                    print("\tYou went over 21, but you have a Ace!")
                    print(f"\tYour cards: {playerCards}, current score: {playerScore}")                
                elif playerScore > 21:
                    # print(f"\tYour cards: {playerCards}, current score: {playerScore}") 
                    print("You went over. You lose")
                    exit()
            else:
                print("\n")
                break
        
        while computerScore < 17:
            deal_card(computerCards)
            computerScore = sum(computerCards)
            if computerScore > 21:
                print(f"\tComputer's cards: {computerCards}, final score: {computerScore}")
                print("Computer went over! You win")
                exit()

        if playerScore == computerScore:
            print(f"\tYour final hand: {playerCards}, final score: {playerScore}")
            print(f"\tComputer's final hand: {computerCards}, final score: {computerScore}")
            print("It's a draw")
        elif playerScore > computerScore:
            print(f"\tYour final hand: {playerCards}, final score: {playerScore}")
            print(f"\tComputer's final hand: {computerCards}, final score: {computerScore}")
            print("You win!")
        else:
            print(f"\tYour final hand: {playerCards}, final score: {playerScore}")
            print(f"\tComputer's final hand: {computerCards}, final score: {computerScore}")
            print("You lose!")

        print("\n*******************************\n*******************************\n")

        should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        if should_continue == 'n':
            start_game = False
    

play_game() 

    





    


