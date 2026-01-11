from Cards.deck import Deck
from Cards.shuffler import RandomShuffler

import random
from Cards.cards import Card

#Logic for the computer in vs computer mode
class ComputerPlayer:
    def __init__(self, difficulty: str):
        self.difficulty = difficulty
        self.seen_cards: list[Card] = []

    #Record the card that was drawn
    def record_card(self, card: Card):
        self.seen_cards.append(card)

    def choose_guess(self, current_card: Card) -> str:
        if self.difficulty == "easy":
            #Easy difficulty randomly selects higher or lower
            return random.choice(["higher", "lower"])

        if self.difficulty == "medium":
            return self.medium_guess(current_card)

        if self.difficulty == "hard":
            return self.hard_guess(current_card)

        raise ValueError("Invalid difficulty")

    #Medium difficulty selects higher if the previous card is less or equal to 8, and picks lower otherwise
    def medium_guess(self, card: Card) -> str:
        if card.rank.value <= 8:
            return "higher"
        return "lower"
    
    #Hard difficulty counts what cards are remaining as the round goes on, picks higher if there are more...
    #... cards above the value of the previous card, and picks lower otherwise
    def hard_guess(self, card: Card) -> str:
        max_rank = 14
        min_rank = 2

        if card.rank.value == min_rank:
            return "higher"
        if card.rank.value == max_rank:
            return "lower"

        #Create the counts with 4 cards per rank
        rank_counts = {}
        for rank in range(min_rank, max_rank + 1):
            rank_counts[rank] = 4

        #Remove the already seen cards and current
        for seen in self.seen_cards:
            rank_counts[seen.rank.value] -= 1

        rank_counts[card.rank.value] -= 1

        higher_remaining = 0
        lower_remaining = 0

        for rank, count in rank_counts.items():
            if rank > card.rank.value:
                higher_remaining += count
            elif rank < card.rank.value:
                lower_remaining += count

        #Print below can validate that computer is making the correct choice
        #print("higher:", higher_remaining, "lower:", lower_remaining)

        #Pick the option with more in it
        return "higher" if higher_remaining >= lower_remaining else "lower"

