import gamelogic.cards

class Player():
    def __init__(self, name, is_bot=False):
        self.name = name
        self.is_bot = is_bot
        self.hand = []

    def draw_initial_cards(self,deck):
        for i in range(7):
            card = gamelogic.cards.deck.draw()
            self.hand.append(card)

    def draw_card(self, deck):
        card = gamelogic.cards.deck.draw()
        self.hand.append(card)
        return card
    
    def play_card(self, card):
        self.hand.remove(card)
        return card