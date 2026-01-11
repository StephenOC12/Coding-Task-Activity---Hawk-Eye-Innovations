from Cards.deck import Deck

def test_deck_has_52_unique_cards():
    deck = Deck()
    cards = deck.get_cards()

    assert len(cards) == 52

    #Check all cards are unique
    unique_cards = {(card.suit, card.rank) for card in cards}
    assert len(unique_cards) == 52
