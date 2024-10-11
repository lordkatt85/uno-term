import random

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __repr__(self):
        return f'Card(color={self.color}, number={self.number})'

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
    
    def create_deck(self):
        colors = ['Red', 'Green', 'Blue', 'Yellow']
        numbers = list(range(10)) + ['Reverse', 'Skip', 'Take Two']
    
        self.cards = [
            Card(color, number)
            for color in colors
            for number in numbers
        ] + [
            Card('Wild', 'Wild') for _ in range(8)
        ] + [
            Card(color, 'Reverse') for color in colors
        ] + [
            Card(color, 'Skip') for color in colors
        ] + [
            Card(color, 'Take Two') for color in colors
        ] + [
            Card('Wild', 'Wild Draw Four') for _ in range(4)
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def __repr__(self):
        return f'Deck(cards={self.cards})'
    
deck = Deck()
deck.shuffle()
print(deck.cards)