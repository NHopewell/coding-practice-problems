"""
deckOfCards.py
==============

Simulate a deck of cards as a Python class


classes:

    Card(symbol, suit):
        properties:
            instance:
                str suit
                str symbol
                
        methods:
            instance:
                __repr__
                
                
    Deck:
    
        properties:
            class:
                List[str] suits
                List[str] symbols
            instance:
                List[Card] deck
                
        methods:
            instance:
                void shuffle
                Card _deal_card()
                List[Card] deal_hand(size: int)
"""
from typing import List, Optional

class Card:
    
    def __init__(self, symbol: str, suit: str):
        
        self.symbol = symbol
        self.suit = suit
        
    def __repr__(self):
        return f"{self.symbol} of {self.suit}"

    
Hand = List[Card]

def new_deck(all_symbols, all_suits):
    
    deck = [Card(symbol, suit) for symbol in all_symbols for suit in all_suits]
    return deck
    
class Deck:
    
    
    all_suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    all_symbols = [
        'Ace', 'King', 'Queen', 'Jack', '10', '9',
        '8', '7', '6', '5', '4', '3', '2']
    
    def __init__(self):
        
        self.deck = new_deck(Deck.all_symbols, Deck.all_suits)
        
    def shuffle(self, ignore: Optional[Hand] = None) -> None:
        
        from random import shuffle
        
        self.deck = new_deck(Deck.all_symbols, Deck.all_suits)
        shuffle(self.deck)
        
        if ignore:
            for card in ignore:
                self.deck.remove(card)
        
    def _deal_card(self) -> Card:
        if len(self.deck) >= 1:
            card = self.deck.pop()
            return card
        return False

    
    def deal_hand(self, size: int) -> Hand:
        
        hand = []
        
        for i in range(size):
            card = self._deal_card()
            if card:
                hand.append(card)
            else:
                self.shuffle(ignore=hand)
                card = self._deal_card()
                hand.append(card)
                
        return hand
            
        
    
    
    
    
##########

if __name__ == "__main__":
    
    deck = Deck()
    
    hand = deck.deal_hand(20)
    print(hand)
    print()
    print(deck.deck)
    
    print()
    
    hand = deck.deal_hand(20)
    print(hand)
    print()
    print(deck.deck)
    
    print()
    
    hand = deck.deal_hand(10)
    print(hand)
    print()
    print(deck.deck)
    
    print()
    
    hand = deck.deal_hand(2)
    print(hand)
    print()
    print(deck.deck)
    
    print()
    
    hand = deck.deal_hand(1)
    print(hand)
    print()
    print(deck.deck)
    print(len(deck.deck))
    