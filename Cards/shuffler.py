import random
from typing import List
from Cards.cards import Card


class Shuffler:
    def shuffle(self, cards: List[Card]) -> List[Card]:
        raise NotImplementedError


class RandomShuffler(Shuffler):
    def shuffle(self, cards: List[Card]) -> List[Card]:
        shuffled = list(cards)
        random.shuffle(shuffled)
        return shuffled


class SeededShuffler(Shuffler):
    def __init__(self, seed: int):
        self._rng = random.Random(seed)

    def shuffle(self, cards: List[Card]) -> List[Card]:
        shuffled = list(cards)
        self._rng.shuffle(shuffled)
        return shuffled
