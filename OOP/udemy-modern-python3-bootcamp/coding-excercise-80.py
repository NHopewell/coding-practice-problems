from random import shuffle
from typing import Optional, Iterable, List

class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

def get_new_deck(Deck):
    new_deck = [
        Card(suit, value) 
            for suit in Deck.possible_suits 
            for value in Deck.possible_values
        ]
    
    return new_deck

class Deck:
    possible_suits = (
        "Hearts", "Diamonds", "Clubs", "Spades")
    possible_values = (
        "A", "2", "3", "4", "5", "6", "7", "8", "9", 
        "10", "J", "Q", "K")
    
    def __init__(self):
        self.deck = get_new_deck(self)
        shuffle(self.deck)
        self.count = len(self.deck)

    def __repr__(self) -> str:
        return f"There are {self.count} cards left in the deck"

    def _replenish_deck(self, exclude: Optional[Iterable[str]] = None):
        self.deck = get_new_deck(self)
        
        if exclude:
            self.deck = [card for card in self.deck if card not in exclude]
        
        self.count = len(self.deck)

    def _update_count(self, num) -> None:
        self.count -= num

    def _deal(self, num_cards: int) -> List[str]:

        if num_cards < self.count:
            hand = self.deck[-num_cards:]
            self.deck = self.deck[:-num_cards]
            self._update_count(num_cards)
        else:
            remainder = num_cards - self.count
            # deal to end
            hand = self.deck[:]
            # replenish deck
            self._replenish_deck(exclude=hand)
            # deal remainder
            if remainder != 0:
                hand += self.deck[-remainder:]
                self.deck = self.deck[:-remainder]
                self._update_count(remainder)
            else:
                self.count = len(self.deck)

        return hand

    def shuffle(self) -> None:
        if self.count < 52:
            msg = "Can only shuffle a full deck of 52 cards."
            raise ValueError(msg)
        else:
            shuffle(self.deck)

    def deal_hand(self, num_cards) -> str:
        return self._deal(num_cards)


deck = Deck()
print(deck.deck)

hand = deck.deal_hand(40)
print(deck.count)

hand2 = deck.deal_hand(10)
print(hand2)
print(deck.count)

hand3 = deck.deal_hand(3)
print(deck.count)

#12
#2
#51

#deck.shuffle()
#print(deck.deck)
