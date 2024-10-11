import random
import json

colors = ["red", "yellow", "green", "blue"]
types = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "draw2", "skip", "reverse", "wild", "wild_draw4"]

class Card():
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def __repr__(self):
        return f"{self.color} {self.type}"
    
class Deck():
    def __init__(self):
        self.cards = self.create_deck()
        random.shuffle(self.cards)

    def create_deck(self):
        deck = []
        
    def draw(self):
        return self.cards.pop() if self.cards else None