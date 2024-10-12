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

if __name__ == "__main__":
    print(Player_list[1].name, lister(Player_list[1].hand))