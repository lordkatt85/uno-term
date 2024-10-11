class Player():
    def __init__(self, name, is_bot=False):
        self.name = name
        self.is_bot = is_bot
        self.hand = []

    def draw_card(self, deck):
        card = deck.draw()
        self.hand.append(card)
        return card
    
    def play_card(self, card):
        self.hand.remove(card)
        return card