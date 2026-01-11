import random
from typing import List
from Cards.cards import Card

# Abstract base class for shuffling strategies
class Shuffler:
    def shuffle(self, cards: List[Card]) -> List[Card]:
        raise NotImplementedError

#Random shuffler for single player with no seed or vs computer
class RandomShuffler(Shuffler):
    def shuffle(self, cards: List[Card]) -> List[Card]:
        shuffled = list(cards)
        random.shuffle(shuffled)
        return shuffled

#Seeded shuffler for playing with someone else
class SeededShuffler(Shuffler):
    def __init__(self, seed: int):
        self._rng = random.Random(seed)

    def shuffle(self, cards: List[Card]) -> List[Card]:
        shuffled = list(cards)
        self._rng.shuffle(shuffled)
        return shuffled
