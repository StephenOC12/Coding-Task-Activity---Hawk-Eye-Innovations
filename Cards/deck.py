from typing import List
from Cards.cards import Card, Suit, Rank


class Deck:
    def __init__(self, include_jokers: bool = False):
        self.include_jokers = include_jokers
        self._cards: List[Card] = []
        self.reset()

    def reset(self) -> None:
        self._cards = [
            Card(suit, rank)
            for suit in Suit
            for rank in Rank
        ]

    def draw(self) -> Card:
        if not self._cards:
            raise RuntimeError("Cannot draw from an empty deck")
        return self._cards.pop()

    def remaining(self) -> int:
        return len(self._cards)

    def get_cards(self) -> List[Card]:
        """Returns a copy for safe external use."""
        return list(self._cards)

    def set_cards(self, cards: List[Card]) -> None:
        """Used by shufflers to replace deck order."""
        self._cards = list(cards)
