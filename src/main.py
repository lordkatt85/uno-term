import gamelogic.cards
import gamelogic.players
from dev_tools import lister

#for cards.py
#this is for you le

#for players.py
n = 2 #number of players
Player_list = ['Player1', 'Player2', 'Player3', 'Player4']

for i in range(n):
    Player_list[i] = gamelogic.players.Player("suren")
    Player_list[i].draw_initial_cards(gamelogic.cards.deck)

game_state = 0

if __name__ == "__main__":
    print(Player_list[1].name, lister(Player_list[1].hand))
    print(gamelogic.cards.deck)
    if game_state == 0:
        print("Welcome to a FanMade Uno game inside the terminal.")
        print("The goal of the game is to get rid of all your cards.")
        print("You can draw cards from the deck, and play them on the board.")
        print("If you don't have a card you want to play, you can draw a new card from the deck.")
        print("You can play a card that you have on the board or a card that you have in your hand.")
        print("You can use any card that you have in your hand or draw a new card from the deck.")
        print("If you don't have a card you want to play, you can draw a new card from the deck.")
        input("when all players are connected, press enter")
        game_state = 1

    while game_state:
        pass