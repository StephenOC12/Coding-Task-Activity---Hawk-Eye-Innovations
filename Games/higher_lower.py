from Cards.deck import Deck
from Cards.shuffler import RandomShuffler, SeededShuffler
from Games.play_vs_computer import ComputerPlayer
import time
from typing import Optional

#Vs Computer mode
def play_higher_lower_vs_computer(difficulty: str):
    deck = Deck()
    shuffler = RandomShuffler()
    deck.set_cards(shuffler.shuffle(deck.get_cards()))

    computer = ComputerPlayer(difficulty)

    current_card = deck.draw()
    computer.record_card(current_card)

    player_score = 0
    computer_score = 0
    player_turn = True  #Player starts - maybe in future could be changed to make it a coin flip

    print(f"Starting card: {current_card}")

    while deck.remaining() > 0:
        #Go until you get one wrong
        run_active = True

        while run_active and deck.remaining() > 0:
            if player_turn:
                print("Your turn")
                guess = input("Higher or lower? ").strip().lower()
                while guess not in ("higher", "lower"):
                    guess = input("Please enter 'higher' or 'lower': ").strip().lower()
            else:
                print("Computer's turn")
                #Sleeps added to prevent the computer taking 5+ goes in under a second, makes the game easier to read
                time.sleep(2)
                guess = computer.choose_guess(current_card)
                print(f"Computer guesses: {guess}")
                time.sleep(2)

            next_card = deck.draw()
            print(f"Next card: {next_card}")

            computer.record_card(next_card)

            if next_card.rank.value == current_card.rank.value:
                print("Equal value — no point, run continues.")
                current_card = next_card
                continue

            #Checking if the guess was correct logic
            if guess == "higher":
                correct = next_card.rank.value > current_card.rank.value
            else:
                correct = next_card.rank.value < current_card.rank.value

            if correct:
                if player_turn:
                    player_score += 1
                    print(f"Correct! Your score: {player_score}")
                else:
                    computer_score += 1
                    print(f"Computer correct! Computer's score: {computer_score}")

                current_card = next_card
            else:
                print("Wrong! Turn ends.")
                current_card = next_card
                #Swap over to computer or back to player
                run_active = False

        player_turn = not player_turn

    #Summary for when the game is finished

    print("\n----- GAME OVER -----")
    print(f"Your score: {player_score}")
    print(f"Computer score: {computer_score}")

    if player_score > computer_score:
        print("You win!")
    elif computer_score > player_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

#Single player mode
def play_higher_lower(seed: Optional[int] = None):
    deck = Deck()

    #Choose either seed or random
    if seed is not None:
        shuffler = SeededShuffler(seed)
    else:
        shuffler = RandomShuffler()

    deck.set_cards(shuffler.shuffle(deck.get_cards()))

    current_card = deck.draw()
    score = 0

    while True:
        print(f"Starting card: {current_card}")
        
        #Ensures valid inputs
        guess = input("Will the next card be higher or lower? ").strip().lower()
        while guess not in ("higher", "lower"):
            guess = input("Please enter 'higher' or 'lower': ").strip().lower()

        next_card = deck.draw()
        print(f"Next card: {next_card}")

        if next_card.rank.value == current_card.rank.value:
            print("Tie! No score change.")
            current_card = next_card
            continue

        if guess == "higher":
            correct = next_card.rank.value > current_card.rank.value
        else:
            correct = next_card.rank.value < current_card.rank.value

        #Update score or finish
        if correct:
            score += 1
            print(f"Correct! Score: {score}")
            current_card = next_card
        else:
            print(f"Wrong! Final score: {score}")
            break
