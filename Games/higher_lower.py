from Cards.deck import Deck
from Cards.shuffler import RandomShuffler, SeededShuffler
from Games.play_vs_computer import ComputerPlayer
import time
from typing import Optional

def play_higher_lower_vs_computer(difficulty: str):
    deck = Deck()
    shuffler = RandomShuffler()
    deck.set_cards(shuffler.shuffle(deck.get_cards()))

    computer = ComputerPlayer(difficulty)

    current_card = deck.draw()
    computer.record_card(current_card)

    player_score = 0
    computer_score = 0
    player_turn = True  # player starts

    print(f"Starting card: {current_card}")

    while deck.remaining() > 0:
        run_active = True

        while run_active and deck.remaining() > 0:
            if player_turn:
                print("Your turn")
                guess = input("Higher or lower? ").strip().lower()
                while guess not in ("higher", "lower"):
                    guess = input("Please enter 'higher' or 'lower': ").strip().lower()
            else:
                print("Computer's turn")
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
                run_active = False

        player_turn = not player_turn

    print("\n----- GAME OVER -----")
    print(f"Your score: {player_score}")
    print(f"Computer score: {computer_score}")

    if player_score > computer_score:
        print("You win!")
    elif computer_score > player_score:
        print("Computer wins!")
    else:
        print("It's a tie!")


def play_higher_lower(seed: Optional[int] = None):
    deck = Deck()

    if seed is not None:
        shuffler = SeededShuffler(seed)
    else:
        shuffler = RandomShuffler()

    deck.set_cards(shuffler.shuffle(deck.get_cards()))

    current_card = deck.draw()
    score = 0

    while True:
        print(f"Starting card: {current_card}")

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

        if correct:
            score += 1
            print(f"Correct! Score: {score}")
            current_card = next_card
        else:
            print(f"Wrong! Final score: {score}")
            break
