from Cards.cards import Card, Suit, Rank
from Games.play_vs_computer import ComputerPlayer

def test_hard_ai_never_guesses_lower_on_two():
    ai = ComputerPlayer("hard")

    card = Card(Suit.HEARTS, Rank.TWO)
    guess = ai.choose_guess(card)

    assert guess == "higher"
